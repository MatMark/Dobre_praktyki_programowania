import javax.swing.*;

public class Field extends JButton {

    private int posX, posY;
    private String letter = ".";

    public Field(String text, int posX, int posY) {
        super(text);
        this.letter = text;
        this.posX = posX;
        this.posY = posY;
    }

    public int getPosX() {
        return posX;
    }

    public void setPosX(int posX) {
        this.posX = posX;
    }

    public int getPosY() {
        return posY;
    }

    public void setPosY(int posY) {
        this.posY = posY;
    }

    public String getLetter() {
        return letter;
    }

    public void setLetter(String letter) {
        this.letter = letter;
        super.setText(letter);
    }

    @Override
    public String toString() {
        return posX + ":" + posY + "| \"" + letter + "\"";
    }

}
