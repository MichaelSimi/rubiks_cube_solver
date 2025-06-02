Welcome!

  You probably know about the classic, iconic puzzle toy, the Rubiks Cube. However, less than 6% of the world's population can solve one! Thats right! The chances are that you cannot solve one. So if you are that person with a Rubik's Cube that has been sitting on your shelf for the past ten years, pick it up, because this project is for you!
  
  Looking up a tutorial is an option. But what if you are that person that is too lazy to learn it? Did you know the world record for solving a Rubik's Cube is under 4 seconds? If that sounds impossible, don’t worry—this project is here to help! I introduce to you: The Rubik's Cube Solver.
  
  As the name suggests, the Rubik's Cube Solver is a code that can solve a Rubik's Cube for you. But how does it work?
  
  The Kociemba library in python is meant to deal with these kind of things. The Kociemba library can solve a Rubik's Cube using two-phase solving, which minimizes the number of moves required to solve it. You just need to type in your cube's state, and it will generate a sequence of moves. When you do those moves, the cube will be solved.

  But can it get easier than that? Well, apparently, yes! With the pygame library I was able to make a Rubik's Cube Solver with an easier way to input the cube state. Here is an overview of all the features:

  Firstly, you will see a 3x3x3 grid. This is to imitate one side of a 3x3 Rubik's Cube. It is where you will put your cube state. The squares on each side of the cube represent the color of the center. For example, when you are putting in the colors for the white side, there will be a red rectangle on the right, a blue one on the top, an orange one on the left, and a green rectangle at the bottom. This helps understand what way the cube should be facing when putting in the state of the cube.

  Once you click a square on the 3x3 grid, a color palette will appear near the top of the screen, with the colors white, red, green, yellow, orange, and blue. Click on one of these, and the square will fill with that color. Keep doing this until the entire grid has a cube state the same as your cube. When you finish, a button saying "next" will appear. Once you click it, it will take you to the next center. Keep doing this until all sides of the cube have been filled.

  Now it will show you the solution. MAKE SURE THAT WHEN YOU ARE DOING THE MOVES, YOU ARE HOLDING THE CUBE WITH GREEN FACING YOU AND WHITE ON THE TOP.

  If an error appears, that probably means that you made a mistake while entering, or that your cube has misplaced pieces or twisted corners. This will make the cube impossible to solve.

That is all there is to say. Enjoy!
