public class Stabel<T> extends Lenkeliste<T> {

    @Override
    public int stoerrelse() {
        return super.stoerrelse();
    }

    @Override
    public void leggTil(int pos, T x) {
        super.leggTil(pos, x);
    }

    @Override
    public void leggTil(T x) {
        super.leggTil(x);
    }

    @Override
    public void sett(int pos, T x) {
        super.sett(pos, x);
    }

    @Override
    public T hent(int pos) {
        return super.hent(pos);
    }

    @Override
    public T fjern(int pos) {
        return super.fjern(pos);
    }

    @Override
    public T fjern() {
        return super.fjern();
    }

    // legg paa slutten av lista
    public void leggPaa(T x) {

        leggTil(stoerrelse(), x);
    }

    // fjern fra slutten av lista
    public T taAv() {

        return fjern(stoerrelse()-1);
    }
}
