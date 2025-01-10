#include "cell.h"

void cell::draw(int row, int col) const
{
	//ANSI control command
	//escape[n;mH moves the cursor to row n, column m
	//1-based, first row is row 1
	std::cout << "\x1b[" << row + 1 << ";" << col + 1 << "H";
	std::cout << (alive ? live_cell : dead_cell);
}
