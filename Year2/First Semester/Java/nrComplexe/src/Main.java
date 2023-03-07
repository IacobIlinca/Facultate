import java.util.ArrayList;
import java.util.List;
import java.util.Objects;

import static java.lang.Integer.parseInt;
import static java.lang.Integer.valueOf;

public class Main {
    public static void main(String[] args) {

        List<NrComplexe> nrs = null;
        nrs = new ArrayList<>();
        NrComplexe rezSuma1 = new NrComplexe(0, 0);
        NrComplexe rezDif1 = new NrComplexe(0, 0);
        NrComplexe rezSuma2 = new NrComplexe(0, 0);
        NrComplexe rezDif2 = new NrComplexe(0, 0);

        List<NrComplexe> componente_rez_suma = null;
        componente_rez_suma = new ArrayList<>();

        List<NrComplexe> componente_rez_dif = null;
        componente_rez_dif = new ArrayList<>();


        //System.out.println(args.length);
        for (int i = 0; i < args.length; i = i + 1) {
            if (i % 2 == 0) {
                String nr = args[i];
                String[] rezultat = nr.split("[+]", 2);
                String re = rezultat[0];
                int reInt = valueOf(re);
                //System.out.println(reInt);
                String im = rezultat[1];
                String[] rezultatI = im.split("i", 2);
                int imInt = valueOf(rezultatI[0]);
                //System.out.println(imInt);

                NrComplexe nr1 = new NrComplexe(reInt, imInt);

                nrs.add(nr1);
                System.out.println(nrs);
            } else {
                if (i == 1) {
                    Operation plus = new Operation('+');
                    Adition suma = new Adition(plus, nrs);
//                    NrComplexe rezSuma1 = new NrComplexe(0,0);
                    rezSuma1 = suma.execute();
                    System.out.println(rezSuma1);
                } else if (Objects.equals(args[i], "+")) {
                    Operation plus = new Operation('+');
                    Adition suma = new Adition(plus, nrs);
//                    NrComplexe rezSuma1 = new NrComplexe(0,0);
                    rezSuma1 = suma.execute();
                    System.out.println(rezSuma1);
                } else if (Objects.equals(args[i], "-")) {
                    Operation minus = new Operation('-');
                    Substraction dif = new Substraction(minus, nrs);
//                    NrComplexe rezDif1 = new NrComplexe(0,0);
                    rezDif1 = dif.execute();
                    System.out.println(rezDif1);
                }
            }
        }
        if (Objects.equals(args[args.length - 2], "+")) {
            Operation plus = new Operation('+');
            Adition suma = new Adition(plus, nrs);
//            NrComplexe rezSuma2 = new NrComplexe(0,0);
            rezSuma2 = suma.execute();
            System.out.println(rezSuma2);
        }
        if (Objects.equals(args[args.length - 2], "-")) {
            Operation minus = new Operation('-');
            Substraction dif = new Substraction(minus, nrs);
//            NrComplexe rezDif2 = new NrComplexe(0,0);
            rezDif2 = dif.execute();
            System.out.println(rezDif2.toString());
        }
//        System.out.println("Rezultatul final este:");
//        System.out.println(rezSuma1);
//        System.out.println(rezSuma2);
//        System.out.println(rezDif1);
//        System.out.println(rezDif2);
//        componente_rez_suma.add(rezSuma1);
//        componente_rez_suma.add(rezSuma2);
////        componente_rez.add(rezDif1);
////        componente_rez.add(rezDif2);
//        Operation plus1 = new Operation('+');
//        Adition suma1 = new Adition(plus1, componente_rez_suma);
//        NrComplexe rezFinal = new NrComplexe(0, 0);
//        rezFinal = suma1.execute();
//        System.out.println(rezFinal);
//
//        componente_rez_dif.add(rezDif1);
//        componente_rez_dif.add(rezDif2);
//        Operation minus1 = new Operation('-');
//        Substraction difF = new Substraction(minus1, nrs);
//        NrComplexe rezDifF = new NrComplexe(0, 0);
//        rezDifF = difF.execute();
//        System.out.println(rezDifF);
//
//

    }
}