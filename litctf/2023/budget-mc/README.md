# rev/budget-mc
If we run `checksec`, we can see this is a pretty standard Linux binary. I then opened it in Ghidra for analysis.
(Note, I've edited some variable names for easier reading, so they might differ from your Ghidra's output)
We can see that it first reads the flag into a buffer at `0x00104160`:
```c
  setbuf(stdin,(char *)0x0);
  setbuf(stdout,(char *)0x0);
  flag_file = fopen("flag.txt","r");
  if (flag_file == (FILE *)0x0) {
    puts("Uh oh! Missing flag.txt file. If this is on the server please contact admin.");
                    /* WARNING: Subroutine does not return */
    exit(1);
  }
  fgets(&flag_buf,0x22,flag_file);
```
Then, we can see that it prints out the map (with some pretty cursed math in the part that generates the character set). Right here we can make note of some important variables like the x/y positions and the map by looking at which addresses are used for those actions. 
```c 
  puts("Your world:");
  for (y = 9; -1 < (int)y; y = y - 1) {
    for (x = 0; (int)x < 0x19; x = x + 1) {
      if ((y == player_y) && (x == player_x)) {
        putchar(L'X');
      }
      else {
        cVar1 = (&map)[(long)(int)y * 0x19 + (long)(int)x];
        putchar((int)s__#!@$%^&*+_00104010
                     [((char)(cVar1 + (((char)((uint)(ushort)(short)cVar1 * 0x67 >> 8) >> 2) -
                                      (cVar1 >> 7)) * -10) + 10) % 10]);
      }
    }
    putchar(10);
  }
  printf("You are currently at position (%d, %d), standing on block id %d.\n",(ulong)player_x,
         (ulong)player_y,
         (ulong)(uint)(int)(char)(&map)[(long)(int)player_y * 0x19 + (long)(int)player_x]);
```
From here I noticed that the map is at `0x00104060`. Maybe we could do a buffer overflow to read off the flag from the "block id" indicator? 

The next part seems like it's dedicated entirely to parsing commands: 
```c 
  printf(">>> ");
  __isoc99_scanf(&%c);
  if (command == 'q') {
    if (local_10 == *(long *)(in_FS_OFFSET + 0x28)) {
      return;
    }
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  if (command == 'm') {
    __isoc99_scanf(&%c);
    if (subcmd1 == 'l') {
      if ((&map)[(long)(int)player_y * 0x19 + (long)(int)(player_x - 1)] != '\x01') {
        player_x = player_x - 1;
        goto fall;
      }
      goto mainloop;
    }
    if ((subcmd1 != 'r') ||
       ((&map)[(long)(int)player_y * 0x19 + (long)(int)(player_x + 1)] == '\x01')) goto mainloop;
    player_x = player_x + 1;
  }
  else {
    if (command == 'j') goto code_r0x001015c7;
    if (command == 'b') {
      __isoc99_scanf(&%c);
      if (subcmd1 == 'l') {
        (&map)[(long)(int)player_y * 0x19 + (long)(int)(player_x - 1)] = 0;
      }
      else {
        if (subcmd1 == 'r') {
          (&map)[(long)(int)player_y * 0x19 + (long)(int)(player_x + 1)] = 0;
          goto fall;
        }
        if (subcmd1 == 'u') {
          (&map)[(long)(int)(player_y + 1) * 0x19 + (long)(int)player_x] = 0;
        }
        else {
          if (subcmd1 != 'd') goto mainloop;
          (&map)[(long)(int)(player_y - 1) * 0x19 + (long)(int)player_x] = 0;
        }
      }
    }
    else if (command == 'p') {
      __isoc99_scanf(&%c,&direction);
      __isoc99_scanf(&%c);
      block1 = subcmd1 + -0x30;
      if ((block1 < 0) || (9 < block1)) goto mainloop;
      if (direction == 'l') {
        (&map)[(long)(int)player_y * 0x19 + (long)(int)(player_x - 1)] = block1;
      }
      else if (direction == 'r') {
        (&map)[(long)(int)player_y * 0x19 + (long)(int)(player_x + 1)] = block1;
      }
      else if (direction == 'u') {
        (&map)[(long)(int)(player_y + 1) * 0x19 + (long)(int)player_x] = block1;
      }
      else {
        if (direction != 'd') goto mainloop;
        (&map)[(long)(int)(player_y - 1) * 0x19 + (long)(int)player_x] = block1;
      }
    }
  }
  goto fall;
code_r0x001015c7:
  if ((&map)[(long)(int)(player_y + 1) * 0x19 + (long)(int)player_x] == 1) goto mainloop;
  __isoc99_scanf(&%c);
  block2 = subcmd1 + -0x30;
  if ((block2 < 0) || (9 < block2)) goto mainloop;
  (&map)[(long)(int)player_y * 0x19 + (long)(int)player_x] = block2;
  player_y = player_y + 1;
fall:
  fall_y = 0;
  while ((&map)[(long)(int)(player_y - 1) * 0x19 + (long)(int)player_x] != '\x01') {
    player_y = player_y - 1;
    fall_y = fall_y + 1;
    if (10 < fall_y) {
      puts("You died from falling too far.");
                    /* WARNING: Subroutine does not return */
      exit(0);
    }
  }
  goto mainloop;
```
It seems like there's all sort of actions that you can do here. There's a lot so let's break it down section-by-section.

There are obviously some boring commands like `q` for quit. Let's look at how we could move around first. Maybe we could find a buffer overflow there.
Indeed, there are basically no restrictions:
```c
  if (command == 'm') {
    __isoc99_scanf(&%c);
    if (subcmd1 == 'l') {
      if ((&map)[(long)(int)player_y * 0x19 + (long)(int)(player_x - 1)] != '\x01') {
        player_x = player_x - 1;
        goto fall;
      }
      goto mainloop;
    }
    if ((subcmd1 != 'r') ||
       ((&map)[(long)(int)player_y * 0x19 + (long)(int)(player_x + 1)] == '\x01')) goto mainloop;
    player_x = player_x + 1;
  }
```
So we can go as far left or right as we want just by issuing `ml` or `mr`. Perfect! Now we can just walk around to the edges of the known universe and have the program just start spitting out the ~~secrets of the universe~~ the flag bytes.

However, it seems like just going right with `mr` triggers weird behavior that causes the player to suddenly be knee-deep in negative y-values. I'm guessing this is very likely because it overruns some important values. So I had to find a faster way to get there, which meant increasing the y-position of the character. (It was pretty tiring anyways to be honest.)

If we go down we find this piece of code that apparently handles jumping (and places a block below you):
```c 
code_r0x001015c7:
  if ((&map)[(long)(int)(player_y + 1) * 0x19 + (long)(int)player_x] == 1) goto mainloop;
  __isoc99_scanf(&%c);
  block2 = subcmd1 + -0x30;
  if ((block2 < 0) || (9 < block2)) goto mainloop;
  (&map)[(long)(int)player_y * 0x19 + (long)(int)player_x] = block2;
  player_y = player_y + 1;
fall:
  fall_y = 0;
  while ((&map)[(long)(int)(player_y - 1) * 0x19 + (long)(int)player_x] != '\x01') {
    player_y = player_y - 1;
    fall_y = fall_y + 1;
    if (10 < fall_y) {
      puts("You died from falling too far.");
                    /* WARNING: Subroutine does not return */
      exit(0);
    }
  }
```
Since `0x30` is ASCII for '0', I assumed that it took a digit as the id number for the block to be placed. I experimented and found out that only '1' worked for some reason.

Anyways, `j1` allowed me to increase the y-position of the characte,r which greatly sped up the process. 

Next I just calculated the difference I needed to travel:
```
0x00104160 - 0x00104060 = 0x100 = 256
```
And then took it mod `0x19 = 25` for how much I needed to increase the x and the y:
```
256 % 25 = 6 
(256 - 6) / 25 = 10 
```
It was then just a matter of traveling there with commands. Specifically, I used `ml` to get to `(6,2)`, then I used `j1` to build a tower until I got to `(6,10)`. It showed me the start of the flag as an ASCII value in decimal:
```
Your world:
      #
      #
      #
      #
      #
      #
      #
      #
#########################
#########################
You are currently at position (6, 10), standing on block id 76.
>>>
```
So then I just kept going on, to `(7,10)`, `(8,10)`, and so on just by using `mr` to move right (i.e. up if we're talking about the addresses) and `j1` to build towers up to `y=10`, and the program continued to leak the bytes to me.
I then just continued moving to the right and building towers of height 10, and I eventually got the entire flag: `LITCTF{w0w_th4t_w4s_fun_w4snt_1t}`.
One major anonyance is that gravity caused me to fall to the ground when I was moving to the next x-value. This is why I recommend this challenge as a good team-building exercise in making dirt towers in a 100% legit CodeTiger approved Minecraft bootleg. I had my other teammate do the odd x-values and I did the even x-values, and it would be a huge performance improvement with 3 people.

