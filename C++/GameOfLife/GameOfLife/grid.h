#ifndef GRID_H
#define GRID_H

#include <string>
#include <vector>
#include <cstdlib>

#include "cell.h"

class grid {
	cell cells[rowmax + 2][colmax + 2];
public:
	void create(int row, int col);

	void draw();

	void randomize();

	bool will_survive(int row, int col);

	bool will_create(int row, int col);

	void update(const grid& next);
};

void calculate(grid& old_gen, grid& new_gen);

#endif // !GRID_H

