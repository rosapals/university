// oblig2 Rosa

public class TestLegemiddel {

    public static void main(String[] args) {

        // legemidler
        Vanlig vann = new Vanlig("h2o", 0, 0.1);
        Narkotisk opium = new Narkotisk("poppyjuice", 500, 0.2, 4);
        Vanedannende sjoko = new Vanedannende("smash", 43, 50.1, 1);

        // testutforing
        System.out.println (testUtenStyrke (vann, 1, "h2o", 0, 0.1));
        System.out.println (testUtenStyrke (opium, 2, "poppyjuice", 500, 0.2) + testHentStyrke (opium, 4));
        System.out.println (testUtenStyrke (sjoko, 3, "smash", 43, 50.1) + testHentStyrke (sjoko, 1));
    }



    // tester toString og andre metoder
    private static String testUtenStyrke(Legemiddel ting, int trorId, String trorNavn, int trorPris, double trorVirke) {

        String tekst = ting.toString() + "\n";
        
        if (ting.hentId() == trorId) { tekst += "hentID OK\n";
        } else { tekst += "hentID ikke OK\n";
        }

        if (ting.hentNavn().equals(trorNavn)) { tekst += "hentNavn OK\n";
        } else { tekst += "hentNavn ikke OK\n";
        }

        if (ting.hentPris() == trorPris) { tekst += "hentPris OK\n";
        } else { tekst += "hentPris ikke OK\n";
        }

        if (ting.hentVirkestoff() == trorVirke) { tekst += "hentVirkestoff OK\n";
        } else { tekst += "hentVirkestoff ikke OK\n";
        }

        if (ting.settNyPris(1) == 1) { tekst += "settNyPris OK\n";
        } else { tekst += "settNyPris ikke OK\n";
        }
        
        return tekst;
    }

    private static String testHentStyrke(Sterk ting, int trorStyrke) {

        String tekst = "";

        if (ting.hentStyrke() == trorStyrke) { tekst += "..hentStyrke OK\n";
        } else { tekst += "..hentStyrke ikke OK\n";
        }

        return tekst;
    }

}
