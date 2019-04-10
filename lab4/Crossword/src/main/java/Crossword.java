import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.FileNotFoundException;
import java.io.IOException;

public class Crossword extends JFrame implements ActionListener {

    private Dictionary dictionary = new Dictionary("src/slowa.txt");
    private JPanel panel;
    private Field [][] fields;
    private Field first;
    private boolean second = false;

    public Crossword(int x, int y) throws HeadlessException, FileNotFoundException {
        super("Crossword " + x + "x" + y);
        fields = new Field[x][y];
        init(x, y);
    }

    private void init(int x, int y) throws FileNotFoundException {

        dictionary.setDictionary("src/slowa.txt");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setSize(60*y, 60*x);

        panel = new JPanel(new GridLayout(x,y,5,5));

        //tworzenie tablicy przycisków
        for(int row = 0; row < x; row ++)
        {
            for(int col = 0; col < y; col ++)
            {
                fields[row][col] = new Field(".",row,col);
                panel.add(fields[row][col]);
                fields[row][col].addActionListener(this);
            }
        }

        setContentPane(panel);
        setVisible(true);
    }




    public void actionPerformed(ActionEvent e) {
        Field source = (Field) e.getSource();
        if(!second) {
            first = source;
            second = true;
        }
        else{
            int fX=first.getPosX(), fY=first.getPosY(), sX=source.getPosX(), sY=source.getPosY();

            //czy są w jednej linii i czy to nie jest to samo pole
            if((fX == sX || fY == sY) && !first.equals(source))
            {
                StringBuilder word = new StringBuilder();
                String result = "";
                int length;

                //poziomo
                if(fX == sX) {

                    int start;
                    if (fY<sY){
                        start = fY;
                    }else start = sY;

                    length = Math.abs(fY-sY)+1;
                    System.out.println("Poziomo: " + length);

                    //odczytanie z pól tekstu
                    for(int i = 0; i<length; i++) { word.append(fields[fX][start + i].getLetter()); }
                    System.out.println(word);
                    //wyszukanie pasującego słowa
                    try {
                       result = dictionary.searchWord(""+word);
                    } catch (IOException e1) {
                        e1.printStackTrace();
                    }
                    //wstawianie słowa ze słownika
                    System.out.println("Wylosowane słowo: " + result);
                    for(int i = 0; i<length; i++) { fields[fX][start + i].setLetter(""+result.charAt(i)); }
                }

                //pionowo
                if(fY == sY) {

                    int start;
                    if (fX<sX){
                        start = fX;
                    }else start = sX;

                    length = Math.abs(fX-sX)+1;
                    System.out.println("Pionowo: " + length);

                    //odczytanie z pól tekstu
                    for(int i = 0; i<length; i++) { word.append(fields[start + i][fY].getLetter()); }
                    System.out.println(word);
                    //wyszukanie pasującego słowa
                    try {
                        result = dictionary.searchWord(""+word);
                    } catch (IOException e1) {
                        e1.printStackTrace();
                    }
                    //wstawianie słowa ze słownika
                    System.out.println("Wylosowane słowo: " + result);
                    for(int i = 0; i<length; i++) { fields[start + i][fY].setLetter(""+result.charAt(i)); }
                }
            }
            else System.out.println("Pola nie są w jednej linii lub wskazano dwa razy to samo pole");
            second = false;
        }
    }

    public static void main(String[] args) throws FileNotFoundException {

        Crossword crossword = new Crossword(7,10);
    }
}
