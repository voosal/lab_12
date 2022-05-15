"""Implemention of the Maze ADT using a 2-D array."""
from arrays import Array2D
from lliststack import Stack


class Maze:
    """Define constants to represent contents of the maze cells."""
    MAZE_WALL = "*"
    PATH_TOKEN = "x"
    TRIED_TOKEN = "o"

    MAZE_NULL = "_"

    def __init__(self, num_rows, num_cols):
        """Creates a maze object with all cells marked as open."""
        self._maze_cells = Array2D(num_rows, num_cols)
        self._start_cell = None
        self._exit_cell = None

    def num_rows(self):
        """Returns the number of rows in the maze."""
        return self._maze_cells.num_rows()

    def num_cols(self):
        """Returns the number of columns in the maze."""
        return self._maze_cells.num_cols()

    def set_wall(self, row, col):
        """Fills the indicated cell with a "wall" marker."""
        assert row >= 0 and row < self.num_rows() and \
               col >= 0 and col < self.num_cols(), "Cell index out of range."
        self._maze_cells[row, col] = self.MAZE_WALL

    def set_start(self, row, col):
        """Sets the starting cell position."""
        assert row >= 0 and row < self.num_rows() and \
               col >= 0 and col < self.num_cols(), "Cell index out of range."
        self._start_cell = _CellPosition(row, col)

    def set_exit(self, row, col):
        """Sets the exit cell position."""
        assert row >= 0 and row < self.num_rows() and \
               col >= 0 and col < self.num_cols(), "Cell index out of range."
        self._exit_cell = _CellPosition(row, col)

    def find_path(self):
        """
        Attempts to solve the maze by finding a path from the starting cell
        to the exit. Returns True if a path is found and False otherwise.
        """
        current_coords = self._start_cell
        self._mark_path(self._start_cell.row, self._start_cell.col)
        stack_of_moves = Stack()
        stack_of_moves.push(self._start_cell)

        while current_coords != self._exit_cell:

            if self._valid_move(current_coords.row - 1, current_coords.col):
                current_coords = self.validate_move(current_coords.row - 1, current_coords.col)
                stack_of_moves.push(current_coords)
            elif self._valid_move(current_coords.row, current_coords.col + 1):
                current_coords = self.validate_move(current_coords.row, current_coords.col + 1)
                stack_of_moves.push(current_coords)
            elif self._valid_move(current_coords.row + 1, current_coords.col):
                current_coords = self.validate_move(current_coords.row + 1, current_coords.col)
                stack_of_moves.push(current_coords)
            elif self._valid_move(current_coords.row, current_coords.col - 1):
                current_coords = self.validate_move(current_coords.row, current_coords.col - 1)
                stack_of_moves.push(current_coords)
            else:
                stack_of_moves.pop()
                self._mark_tried(current_coords.row, current_coords.col)
                try:
                    current_coords = stack_of_moves.peek()
                except AssertionError:
                    return False

        return True

    def validate_move(self, row, col):
        current_coords = _CellPosition(row, col)
        self._mark_path(row, col)

        return current_coords

    def reset(self):
        """Resets the maze by removing all "path" and "tried" tokens."""
        for row_num in range(self.num_rows()):
            for col_num in range(self.num_cols()):
                if self._maze_cells.__getitem__((row_num, col_num)) != self.MAZE_WALL:
                    self._maze_cells.__setitem__((row_num, col_num), self.MAZE_NULL)

    def __str__(self):
        """Returns a text-based representation of the maze."""
        return_str = ''
        for row_num in range(self.num_rows()):
            for col_num in range(self.num_cols()):
                if self._maze_cells.__getitem__((row_num, col_num)) == None:
                    return_str += self.MAZE_NULL + ' '
                else:
                    return_str += self._maze_cells.__getitem__((row_num, col_num)) + ' '
            return_str += "\n"

        return return_str[:-1]

    def _valid_move(self, row, col):
        """Returns True if the given cell position is a valid move."""
        return row >= 0 and row < self.num_rows() \
               and col >= 0 and col < self.num_cols() \
               and self._maze_cells[row, col] is None

    def _exit_found(self, row, col):
        """Helper method to determine if the exit was found."""
        return row == self._exit_cell.row and col == self._exit_cell.col

    def _mark_tried(self, row, col):
        """Drops a "tried" token at the given cell."""
        self._maze_cells[row, col] = self.TRIED_TOKEN

    def _mark_path(self, row, col):
        """Drops a "path" token at the given cell."""
        self._maze_cells[row, col] = self.PATH_TOKEN


class _CellPosition(object):
    """Private storage class for holding a cell position."""
    def __init__(self, row, col):
        self.row = row
        self.col = col

    def __eq__(self, other):
        return self.row == other.row and self.col == other.col
