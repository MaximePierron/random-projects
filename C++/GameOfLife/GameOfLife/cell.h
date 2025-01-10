#ifndef CELL_H
#define CELL_H

#include <iostream>
#include "life.h"

class cell {
	//cell status
	bool alive;
public:
	cell(): alive(false) {}

	void draw(int row, int col) const;

	void create() {
		alive = true;
	}

	void destroy() {
		alive = false;
	}

	bool is_alive() const { return alive;  }
};

#endif // !CELL_H

