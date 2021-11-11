// elementene som settes inn skal vaere sammenlignbare
public class SortertLenkeliste<T extends Comparable<T>> extends Lenkeliste<T> {

    @Override
    public int stoerrelse() {
        return super.stoerrelse();
    }

    @Override
    public void leggTil(int pos, T x) throws UnsupportedOperationException {
        throw new UnsupportedOperationException();
    }

    @Override
    public void leggTil(T x) {

        T nyNodeData = x;

        // lista er tom
        if (stoerrelse() == 0) {
            super.leggTil(nyNodeData);
        }

        // start node er storre eller lik ny node
        else if (start.data.compareTo(nyNodeData) >= 0) {
            super.leggTil(0, nyNodeData);
        }

        // ny node er storre eller lik slutt node
        else if (nyNodeData.compareTo(slutt.data) >= 0) {
            super.leggTil(nyNodeData);
        }

        // iter gjennom listen til nyNode er mindre enn peker
        else {
            Node peker = start;
            int nyNodeIndeks = 0;

            while (nyNodeData.compareTo(peker.data) > 0) {
                peker = peker.neste;
                nyNodeIndeks ++;
            }
            super.leggTil(nyNodeIndeks, nyNodeData);
        }
    }

    @Override
    public void sett(int pos, T x) throws UnsupportedOperationException {
        throw new UnsupportedOperationException();
    }

    @Override
    public T hent(int pos) {
        return super.hent(pos);
    }

    @Override
    public T fjern(int pos) {
        if (pos == 0) {
            return super.fjern();
        }
        return super.fjern(pos);
    }

    // fjerner siste element i lista
    @Override
    public T fjern() {
        return fjern(stoerrelse()-1);
    }

}
