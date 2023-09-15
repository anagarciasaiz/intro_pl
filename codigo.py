# import necessary OR tools
from ortools.linear_solver import pywraplp
solver = pywraplp.Solver('Maximize army power', pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)


# create the VARIABLES we want to optimize
swordsmen = solver.IntVar(0, solver.infinity(), 'swordsmen')
bowmen = solver.IntVar(0, solver.infinity(), 'bowmen')
horsemen = solver.IntVar(0, solver.infinity(), 'horsemen')

# add CONSTRAINTS for our resources
# the sum of each resource used by each unit type must be less than the total amount of that resource available
solver.Add(swordsmen*60 + bowmen*80 + horsemen*140 <= 1200)  # food
solver.Add(swordsmen*20 + bowmen*10 <= 800)  # wood
solver.Add(bowmen*40 + horsemen*100 <= 600)  # gold

# MAXIMIZE the objective function
solver.Maximize(swordsmen*70 + bowmen*95 + horsemen*230)


# SOLVE the problem
status = solver.Solve()
# If an optimal solution has been found, print results
if status == pywraplp.Solver.OPTIMAL:
    print('================= Solution =================')
    print(f'Solved in {solver.wall_time():.2f} milliseconds in {solver.iterations()} iterations')
    print()
    print(f'Optimal power = {solver.Objective().Value()} 💪 power')
    print('Army:')
    print(f' - 🗡️ Swordsmen = {swordsmen.solution_value()}')       
    print(f' - 🏹 Bowmen = {bowmen.solution_value()}')       
    print(f' - 🐎 Horsemen = {horsemen.solution_value()}') 

# If no optimal solution has been found, print the status
else:
    print('The solver could not find an optimal solution.')