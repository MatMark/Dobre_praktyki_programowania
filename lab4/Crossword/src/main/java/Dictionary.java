import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class Dictionary {

    private BufferedReader dictionary = null;
    private String source;
    private List<String> lengthDict = null;
    private List<String> patternDict = null;

    public Dictionary(String source) {
        this.source = source;
    }

    public void setDictionary(String source) throws FileNotFoundException {
        dictionary = new BufferedReader(new FileReader(source));
    }

    //wczytanie słów o pasującej długości do listy
    private List<String> lengthTest(String pattern) throws IOException {
        setDictionary(source);
        List<String> tmpList = new ArrayList<String>();
        try {
            String l = dictionary.readLine();
            while (l != null) {
                if(l.length() == pattern.length()) tmpList.add(l);
                l = dictionary.readLine();
            }
        } finally {
            if (dictionary != null) {
                dictionary.close();
            }
        }
        return tmpList;
    }

    //sprawdzenie wzorca ze słowami z listy ze słowami o pasującej długości
    private List<String> patternTest(String pattern)
    {
        List<String> tmpList = new ArrayList<String>();
        for (int i=0; i<lengthDict.size(); i++) { if(lengthDict.get(i).matches(pattern)) tmpList.add(lengthDict.get(i)); }
        return tmpList;
    }

    //wyszukanie pasujących słów i wylosowanie jednego
    //jeżeli nie pasuje żadne słowo to zwraca wzorzec
    //symbolem oznaczającym dowolny znak jest "." [kropka]
    public String searchWord(String pattern) throws IOException {
        lengthDict = lengthTest(pattern);
        patternDict = patternTest(pattern);
        String word;
        if(!patternDict.isEmpty()) word = patternDict.get(new Random().nextInt(patternDict.size()));
        else word = pattern;
        System.out.println("Wszystkie pasujące: " + patternDict);
        return word;
    }

    public static void main(String[] args) {
        Dictionary test = new Dictionary("src/slowa.txt");
    }
}
