using std::vector;
using std::string;
using std::set;

class CosGUIViewOnly :public QWidget, public Observer {
    FilmeServ& serv;
    void initialize() {
        serv.addObserver(this);
    }
    void paintEvent(QPaintEvent*) override {
        QPainter painter{ this };

        for (auto film : serv.getAlldincos_serv())
        {
            int x, y;

            x = rand() % 400 + 1;
            y = rand() % 400 + 1;
            qDebug() << x << " " << y;
            QRectF target(x, y, 100, 94);
            QRectF source(0, 0, 732, 720);
            QImage image("film.jpg");

            //painter.fillRect(x,y,50,50,Qt::GlobalColor::red);

            painter.drawImage(target, image, source);

            x += 40;

        }
    }
    void update() override {
        repaint();
    }

public:
    CosGUIViewOnly(FilmeServ& serv) :serv{ serv } {
        initialize();
    };

    ~CosGUIViewOnly() {
        serv.removeObserver(this);
    }
};