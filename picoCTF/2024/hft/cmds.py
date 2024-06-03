class VmmapVar(gdb.Command):
    def __init__(self):
        super(VmmapVar, self).__init__("vmmap_var", gdb.COMMAND_USER)

    def invoke(self, arg, from_tty):
        try:
            rax_value = int(gdb.parse_and_eval(arg))
            gdb.execute("vmmap {}".format(hex(rax_value)))
        except gdb.error as e:
            print("Error:", e)

VmmapVar()

