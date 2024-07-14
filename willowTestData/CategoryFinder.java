import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class CategoryFinder {

    public static void main(String[] args) {
        String tsvFilePath = "/home/abera/data1/data1/combined_subset_10x10.tsv";

        try {
            // Load and process TSV file
            List<List<String>> data = loadDataFromTSV(tsvFilePath);

            // Debug: Print the loaded data
            System.out.println("Loaded data:");
            for (List<String> row : data) {
                System.out.println(row);
            }

            // Find category 0 in column 1
            int categoryToFind = 0;
            int columnIndex = 1;
            String foundValue = findCategoryInColumn(data, categoryToFind, columnIndex);
            System.out.println("Found value: " + foundValue);
        } catch (IOException e) {
            e.printStackTrace();
        } catch (IllegalArgumentException e) {
            System.err.println(e.getMessage());
        }
    }

    public static List<List<String>> loadDataFromTSV(String tsvFilePath) throws IOException {
        List<List<String>> data = new ArrayList<>();
        BufferedReader reader = new BufferedReader(new FileReader(tsvFilePath));
        String line;
        while ((line = reader.readLine()) != null) {
            String[] columns = line.split("\t");
            data.add(Arrays.asList(columns));
        }
        reader.close();
        return data;
    }

    public static String findCategoryInColumn(List<List<String>> data, int category, int columnIndex) {
        for (List<String> row : data) {
            // Debug: Print the row being processed
            System.out.println("Processing row: " + row);
            if (row.size() > columnIndex && row.get(columnIndex).equals(String.valueOf(category))) {
                return row.get(columnIndex);
            }
        }
        throw new IllegalArgumentException("Didn't find the specified category <" + category + "> in col <" + columnIndex + ">");
    }
}

