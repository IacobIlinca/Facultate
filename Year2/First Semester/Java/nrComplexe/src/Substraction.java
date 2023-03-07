import java.util.List;

public class Substraction extends ComplexExpression {

    public Substraction(Operation operation, List<NrComplexe> args) {
        super(operation, args);
    }

    @Override
    public NrComplexe execute() {
        int k;
        NrComplexe dif = new NrComplexe(0, 0);
        for (k = 0; k < args.size(); k++) {
            dif = NrComplexe.scadere(dif, args.get(k));

        }
        return dif;

    }
}
