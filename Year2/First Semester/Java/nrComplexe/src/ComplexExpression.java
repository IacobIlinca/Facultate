import java.util.ArrayList;
import java.util.List;

public abstract class ComplexExpression {

    private Operation operation;
    protected List<NrComplexe> args = new ArrayList<>();

    /**
     *
     * @param operation
     * @param args
     */
    public ComplexExpression(Operation operation, List<NrComplexe> args) {
        this.operation = operation;
        this.args = args;
    }

    public abstract NrComplexe execute();

}
