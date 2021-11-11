// oblig2 Rosa

public class TestResepter {

    public static void main(String[] args) {

        // legemidler
        Vanlig evian = new Vanlig("h2o", 200, 0.1);
        Vanedannende sjoko = new Vanedannende("smash", 43, 50.1, 1);

        // lege
        Lege drProktor = new Lege("drProktor");

        // resepter
        Hvit r1 = new Hvit(evian, drProktor, 3105, 1);
        PResept r2 = new PResept(sjoko, drProktor, 3435);
        Militaer r3 = new Militaer(sjoko, drProktor, 007, 2);
        Blaa r4 = new Blaa(evian, drProktor, 1213, 0);

        // testutforing
        System.out.println (enhetsTest (r1, evian, 1, drProktor, 3105, 1, 200, true, "hvit"));
        System.out.println (enhetsTest (r2, sjoko, 2, drProktor, 3435, 3, 0, true, "hvit"));
        System.out.println (enhetsTest (r3, sjoko, 3, drProktor, 007, 2, 0, true, "hvit"));
        System.out.println (enhetsTest (r4, evian, 4, drProktor, 1213, 0, 50, false, "blaa"));
    }

    // tester toString og andre metoder
    private static String enhetsTest(Resept resept, Legemiddel trorLegemiddel, int trorId, Lege trorLege, int trorPasientId,
                   int trorReit, int trorPrisAaBetale, boolean trorBruk, String trorFarge) {

        String tekst = resept.toString();

        if (resept.hentLegemiddel() == trorLegemiddel) { tekst += "\nhentLegemiddel OK\n";
        } else { tekst += "\nhentLegemiddel ikke OK\n";
        }

        if (resept.hentId() == trorId) { tekst += "hentId OK\n";
        } else { tekst += "hentId ikke OK\n";
        }

        if (resept.hentLege() == trorLege) { tekst += "hentLege OK\n";
        } else { tekst += "hentLege ikke OK\n";
        }

        if (resept.hentPasientId() == trorPasientId) { tekst += "hentPasientId OK\n";
        } else { tekst += "hentPasientId ikke OK\n";
        }

        if (resept.hentReit() == trorReit) { tekst += "hentReit OK\n";
        } else { tekst += "hentReit ikke OK\n";
        }

        if (resept.prisAaBetale() == trorPrisAaBetale) { tekst += "prisAaBetale OK\n";
        } else { tekst += "prisAaBetale ikke OK\n";
        }

        if (resept.bruk() == trorBruk) { tekst += "bruk OK\n";
        } else { tekst += "bruk ikke OK\n";
        }

        if (resept.hentFarge() == trorFarge) { tekst += "hentFarge OK\n";
        } else { tekst += "hentFarge ikke OK\n";
        }

        return tekst;
    }
    
}
