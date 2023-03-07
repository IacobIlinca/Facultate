import static java.lang.Math.abs;

public class NrComplexe {

    private int re;
    private int im;

    public NrComplexe(int re, int im) {
        this.re = re;
        this.im = im;
    }

    public int getRe() {
        return re;
    }

    public int getIm() {
        return im;
    }

    @Override
    public String toString() {
        if(re>0 && im>0){
        return re + "+" + im + "*i"; }

        else if(re<0 && im>0) {
            return "-" + re + "+" + im + "*i";
        }
        else if(re>0 && im<0) {
            return re + "+" +"-" +  im + "*i";
        }
        else {
            return "-" + re + "-" +  im + "*i";
        }
    }

    public static NrComplexe adunare(NrComplexe nr1, NrComplexe nr2) {
        int reNou;
        int imNou;
        //partea reala
        if (nr1.getRe() > 0 && nr2.getRe() > 0) {
            reNou = nr1.getRe() + nr2.getRe();
        } else if (nr1.getRe() < 0 && nr2.getRe() > 0) {
            reNou = nr2.getRe() - nr1.getRe();
        } else if (nr1.getRe() < 0 && nr2.getRe() < 0) {
            reNou = nr1.getRe();
            reNou = reNou - nr2.getRe();
            reNou = reNou - nr1.getRe();
        } else if (nr1.getRe() > 0 && nr2.getRe() < 0)
        {
            reNou = nr1.getRe() - nr2.getRe();
        }
        else if(nr1.getRe() > 0 && nr2.getRe() == 0){
            reNou = nr1.getRe();
        }
        else if(nr1.getRe() ==0 && nr2.getRe() > 0){
            reNou = nr2.getRe();
        }
        else if(nr1.getRe() < 0 && nr2.getRe() == 0){
            reNou = nr1.getRe();
        }
        else if(nr1.getRe() ==0 && nr2.getRe() < 0){
            reNou = nr2.getRe();
        }
        else {
            reNou = 0;
        }


        //partea imaginara
        if (nr1.getIm() > 0 && nr2.getIm() > 0) {
            imNou = nr1.getIm() + nr2.getIm();
        } else if (nr1.getIm() < 0 && nr2.getIm() > 0) {
            imNou = nr2.getIm() - nr1.getIm();
        } else if (nr1.getIm() < 0 && nr2.getIm() < 0) {
            imNou = nr1.getIm();
            imNou = imNou - nr2.getIm();
            imNou = imNou - nr2.getIm();
        } else if (nr1.getIm() > 0 && nr2.getIm() < 0)
        {
            imNou = nr1.getIm() - nr2.getIm();
        }
        else if(nr1.getIm() > 0 && nr2.getIm() == 0){
            imNou = nr1.getIm();
        }
        else if(nr1.getIm() ==0 && nr2.getIm() > 0){
            imNou = nr2.getIm();
        }
        else if(nr1.getIm() < 0 && nr2.getIm() == 0){
            imNou = nr1.getIm();
        }
        else if(nr1.getIm() ==0 && nr2.getIm() < 0){
            imNou = nr2.getIm();
        }
        else {
            imNou = 0;
        }


        NrComplexe nrNou = new NrComplexe(reNou, imNou);
        return nrNou;
    }

    public static NrComplexe scadere(NrComplexe nr1, NrComplexe nr2) {
        int reNou;
        int imNou;
        //partea reala
        if (nr1.getRe() < 0 && nr2.getRe() < 0) {
            reNou = nr1.getRe() + abs(nr2.getRe());
        }

        else if (nr1.getRe() > 0 && nr2.getRe() > 0) {
                reNou = nr1.getRe() - nr2.getRe();

        }

        else if (nr1.getRe() < 0 && nr2.getRe() > 0) {
                reNou = nr2.getRe() + nr1.getRe();

        }

        else if (nr1.getRe() > 0 && nr2.getRe() < 0) {
                reNou = nr1.getRe() + abs(nr2.getRe());


        }
        else if (nr1.getRe() == 0 && nr2.getRe() >0) {
            reNou = 0-nr2.getRe();
        }
        else if (nr1.getRe() == 0 && nr2.getRe() <0) {
            reNou = nr2.getRe();
        }
        else if (nr1.getRe() > 0 && nr2.getRe() == 0) {
            reNou = nr1.getRe();
        }
        else if (nr1.getRe() < 0 && nr2.getRe() == 0) {
            reNou = nr1.getRe();
        }
        else {
            reNou = 0;
        }

        //partea imaginara
        if (nr1.getIm() < 0 && nr2.getIm() < 0) {
            imNou =  nr1.getIm() + abs(nr2.getIm());
        }

        else if (nr1.getIm() > 0 && nr2.getIm() > 0) {
                imNou = nr1.getIm() - nr2.getIm();

        }

        else if (nr1.getIm() < 0 && nr2.getIm() > 0) {
                imNou = nr2.getIm() + nr1.getIm();
            }
        else if (nr1.getIm() > 0 && nr2.getIm() < 0) {
                imNou = nr1.getIm() + abs(nr2.getIm());


        }
        else if (nr1.getIm() == 0 && nr2.getIm() >0) {
            imNou = 0-nr2.getIm();
        }
        else if (nr1.getIm() == 0 && nr2.getIm() <0) {
            imNou = nr2.getIm();
        }
        else if (nr1.getIm() > 0 && nr2.getIm() == 0) {
            imNou = nr1.getIm();
        }
        else if (nr1.getIm() < 0 && nr2.getIm() == 0) {
            imNou = nr1.getIm();
        }
        else {
            imNou = 0;
        }

        //if(reNou<0) reNou = 0-reNou;
        NrComplexe nrNou = new NrComplexe(reNou, imNou);
        return nrNou;
    }


}
