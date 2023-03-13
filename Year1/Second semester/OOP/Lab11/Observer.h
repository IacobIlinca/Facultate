#include <vector>
#include <algorithm>
using std::remove;


class Observer {
public:
    virtual void update() = 0;
};


class Observable {
private:
    std::vector<Observer*> observers;
public:

    void notify() {
        for (auto observer : observers)
        {
            observer->update();
        }
    }

    void removeObserver(Observer* this_observer)
    {
        observers.erase(remove(observers.begin(), observers.end(), this_observer), observers.end());
    }

    void addObserver(Observer* observer)
    {
        observers.push_back(observer);
    }
};