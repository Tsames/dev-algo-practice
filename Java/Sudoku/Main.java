package Java.Sudoku;

public class Main {
    public static void main(String[] args) {
        Sudoku sudoku = new Sudoku();
        System.out.println(sudoku);
    }
}

class Tile {
    private final byte id;
    private byte value;
    private final byte sqr;
    private final byte col;
    private final byte row;

    public Tile(byte tileId, byte value) {
        this.id = tileId;
        this.value = value;
        this.sqr = calculateSqr(tileId);
        this.col = calculateCol(tileId);
        this.row = calculateRow(tileId);
    }

    public Tile(byte tileId) {
        this(tileId, (byte) 0);
    }

    private byte calculateSqr(byte tileId) {
        return (byte) (tileId / 9);
    }

    private byte calculateCol(byte tileId) {
        // Calculate the square's column
        byte sqrModulo = (byte) (this.sqr % 3);

        // Calculate the number of columns over from the first tile in the square
        byte tilesFromFirstTile = (byte) ((tileId % 9) % 3);

        return (byte) ((sqrModulo * 3) + tilesFromFirstTile);
    }

    private byte calculateRow(byte tileId) {
        // Calculate the square's row
        byte sqrRow = (byte) (this.sqr / 3);

        // Calculate the number of rows over from the first tile in the square
        byte tileRow = (byte) ((tileId % 9) / 3);

        return (byte) ((sqrRow * 3) + tileRow);
    }

    @Override
    public String toString() {
        return "Tile [" + value + "] - Square: " + sqr + " / Row: " + row + " / Column: " + col;
    }
}

class Sudoku {
    private final Tile[] board = new Tile[81];

    public Sudoku() {
        for (int i = 0; i < board.length; i++) {
            board[i] = new Tile((byte) i);
        }
    }

    // private byte calculateRow(byte tileId) {
    //     // Calculate the square's row
    //     byte sqrRow = (byte) (this.sqr / 3);

    //     // Calculate the number of rows over from the first tile in the square
    //     byte tileRow = (byte) ((tileId % 9) / 3);

    //     return (byte) ((sqrRow * 3) + tileRow);
    // }

    @Override
    public String toString() {
        StringBuilder result = new StringBuilder();
        for (Tile tile : board) {
            result.append(tile).append("\n");
        }
        return result.toString();
    }
}