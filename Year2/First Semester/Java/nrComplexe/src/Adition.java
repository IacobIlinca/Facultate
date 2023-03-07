import java.util.List;

public class Adition extends ComplexExpression {

    public Adition(Operation operation, List<NrComplexe> args) {
        super(operation, args);
    }

    @Override
    public NrComplexe execute() {
        int k;
        NrComplexe suma = new NrComplexe(0, 0);
        for (k = 0; k < args.size(); k++) {
            suma = NrComplexe.adunare(suma, args.get(k));

        }
        return suma;
        //System.out.println(args.get(0));
        //System.out.println(args.get(1));
    }
}
