# misc/So You Think You Can Talk
For this challenge, the goal was to reply to other people's messages such that ChatGPT rated the reply to be "helpful". You would get points for "helpful" messages and lose points for "unhelpful" messages.
This was the code used to rate responses in the bot:
```javascript
client.on("messageCreate", async (msg) => {
  if(msg.content.length > 2000) return;
  if(msg.channelId == 1137653157825089536) {
    // Within the right channel
    user_id = msg.author.id;
    if(!users.has(user_id)) {
      users.set(user_id,new User(msg.author.globalName));
    }

    if(users.get(user_id).disabled) return;

    if(msg.mentions.repliedUser) {
      const repliedTo = await msg.channel.messages.fetch(msg.reference.messageId);
      if(repliedTo.content.length > 2000) return;
      if(repliedTo.author.id == msg.author.id) return;
      if(msg.createdTimestamp - repliedTo.createdTimestamp <= 2 * 60000) { // 2 minutes of time
        if(await check(msg.content,repliedTo.content)) {
          // Yay successfully earn point
          users.get(user_id).score += 1;
          users.get(repliedTo.author.id).score = Math.max(users.get(repliedTo.author.id).point - 0.4,0);
          msg.react('😄');

        }else{
          // Nope, you get points off
          users.get(user_id).score = Math.max(users.get(user_id).score - 0.4,0);
          msg.react('😭');
        }
      }
    }else{
      // [redacted]
    }
  }
});
```
At first, I tried manually composing responses, but I realized that the bot's definition of "helpful" was ambiguous. It was difficult to consistently compose "helpful" messages because I was dealing with an unknown black-box function for checking the text and because of the randomness of the LLM model.

Then I realized that if I used a GPT model to write questions and responses, I would probably have a high probability of getting rated because the standards that ChatGPT rates responses by is probably the same as the ones that it uses to write "helpful responses". Basically, I dogfooded text from ChatGPT back into the conversation.

So then I got one of my teams members to help me simulate a two-sided conversation. I would create some question for ChatGPT to answer (the process was greatly assisted by [Poe.com](https://poe.com)'s suggestions feature), and I would send it to my team members. Then, they would send it in the Discord channel and I replied to it.

After a lot of question asking and answering (and some luck, because it was early in the game and there were less constraints at the time), the bot declared my win and I got the flag: `LITCTF{Huh_1_gu3s5_u_R34lly_c4n_t4lk_4ft3ral1}`.

