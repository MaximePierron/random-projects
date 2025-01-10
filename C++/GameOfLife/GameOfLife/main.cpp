#include "grid.h"
#include <iostream>
#include "ansi_escapes.h"

int main(int argc, char* argv[]) {
	std::cout << "Conway's game of life\n";
	std::cout << "Press the return key to display each generation\n";

	std::cin.get();
	setupConsole();

	//first gen
	grid current_generation;

	//random populate
	current_generation.randomize();

	while (true) {
		//draw current gen
		current_generation.draw();

		std::cin.get();

		//next gen grid
		grid next_generation;

		//populate next gen
		calculate(current_generation, next_generation);

		//update
		current_generation.update(next_generation);
	}

	std::cout << "\x1b[" << 0 << ";" << rowmax - 1 << "H";
	restoreConsole();
}