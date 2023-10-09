import angr 
target = angr.Project('./x0rr3al', main_opts={'base_addr': 0}, auto_load_libs=False)
final = 0x1b62
wrong = [0x156a, 0x16ad]
entry_state = target.factory.entry_state(args=['./x0rr3al'])
simulation = target.factory.simulation_manager(entry_state)
simulation.explore(find = final, avoid = wrong)
solution = simulation.found[0].posix.dumps(0)
print(solution)
