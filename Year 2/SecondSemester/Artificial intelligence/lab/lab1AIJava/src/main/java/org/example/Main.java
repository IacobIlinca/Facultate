package org.example;

import java.util.*;


public class Main {

    /**
     * determina ultimul cuvant dpdv alfabetic
     *
     * @param prop: propozitia in care se cauta cuvantul
     * @return : ultimul cuvant dpdv alfabetic
     */
    public static String p1(String prop) {
        String[] words = prop.split(" ");
        String max = words[0];
        for (String word : words) {
            if (word.compareTo(max) > 0) {
                max = word;
            }
        }
        return max;
    }

    /**
     * determina distanta Euclidiana intre 2 locatii
     *
     * @param loc1: una dintre locatii
     * @param loc2: cea de a doua locatie
     * @return: distanta dintre cele 2 locatii oferite
     */
    public static double p2(List<Integer> loc1, List<Integer> loc2) {
        return Math.sqrt(((loc1.get(0) - loc2.get(0)) * (loc1.get(0) - loc2.get(0))) + ((loc1.get(1) - loc2.get(1)) * (loc1.get(1) - loc2.get(1))));

    }

    /**
     * determina produsul scalar a 2 vectori rari de nr reale
     *
     * @param vect1: unul dintre vectorii rari
     * @param vect2: cel de al doilea vector rar
     * @return: produsul scalar dintre cele 2 locatii
     */

    public static int p3(List<Integer> vect1, List<Integer> vect2) {
        int prod = 0;
        for (int i = 0; i < vect1.size(); i++) {
            {
                if (vect1.get(i) != 0 || vect2.get(i) != 0) {
                    prod += vect1.get(i) * vect2.get(i);
                }
            }
        }
        return prod;
    }

    /**
     * determina cuvintele care apar exct o data
     *
     * @param prop: textul a carui cuvinte se analizeaza
     */
    public static void p4(String prop) {
        String[] words = prop.split(" ");
        Map<String, Integer> map = new HashMap<String, Integer>();
        for (String word : words) {
            map.merge(word, 1, Integer::sum);
        }

        for (Map.Entry<String, Integer> e : map.entrySet()) {
            if (e.getValue() == 1) {
                System.out.println(e.getKey());
            }
        }
    }

    /**
     * sa se determine valoarea care se repeta de 2 ori
     *
     * @param n:    nr de elemente din lista
     * @param list: lista in care se cauta duplicatele
     * @return: valoarea care se repeta
     */
    public static int p5(Integer n, List<Integer> list) {
        Map<Integer, Integer> map = new HashMap<>();
        for (Integer val : list) {
            map.merge(val, 1, Integer::sum);
        }
        for (Map.Entry<Integer, Integer> e : map.entrySet()) {
            if (e.getValue() == 2) {
                return e.getKey();
            }
        }
        return 0;
    }

    /**
     * sa se determine elementul majoritar
     *
     * @param list: lista in care se cauta
     * @return: elementul majoritar al listei date
     */
    public static int p6(List<Integer> list) {
        Map<Integer, Integer> map = new HashMap<>();
        for (Integer val : list) {
            map.merge(val, 1, Integer::sum);
        }
        //Map.Entry<Integer, Integer> max = null;
        int max = 0, poz = 0;
        for (Map.Entry<Integer, Integer> e : map.entrySet()) {
            if (e.getValue() > max && e.getValue() > list.size() / 2) {
                poz = e.getKey();
                max = e.getValue();
            }
        }
        return poz;
    }

    /**
     * plaseaza toate elementele mai mici decta pivotul in stanga sa, iar pe cele mai mari in dreapta
     *
     * @param arr:  lista de elemente
     * @param low:  pozitita de start
     * @param high: pozitia de final
     * @return: pivotul
     */
    static int partition(List<Integer> arr, int low, int high) {
        int pivot = arr.get(high);

        int i = (low - 1);

        for (int j = low; j <= high - 1; j++) {

            if (arr.get(j) < pivot) {
                i++;
                Collections.swap(arr, i, j);
            }
        }
        Collections.swap(arr, i + 1, high);
        return (i + 1);
    }

    /**
     * functia de sortare utilizand metoda QuickSort
     *
     * @param arr:lista  initiala
     * @param low:       index de inceput
     * @param high:index de final
     */
    static void quickSort(List<Integer> arr, int low, int high) {
        if (low < high) {
            int pi = partition(arr, low, high);
            quickSort(arr, low, pi - 1);
            quickSort(arr, pi + 1, high);
        }
    }

    /**
     * al k-lea cel mai mare element din lista
     *
     * @param list: lista initiala
     * @param k:    a cata pozitie se doreste
     * @return: al k-lea element
     */
    public static int p7(List<Integer> list, Integer k) {
        quickSort(list, 0, list.size() - 1);
        Set<Integer> set = new HashSet<>(list);
        int j = 0;
        for (Integer i : set) {
            if (j == set.size() - k) {
                return i;
            }
            j++;
            //System.out.println(i);
        }
        return 0;
    }

    /**
     * determina indexul liniei  care contine cele mai multe elemente 1
     *
     * @param matrix: matricea care se da, sortata crescator pe linii
     * @param m:      numarul de linii din matrice
     * @param n:      numarul de coloane din matrice
     * @return: indexul cu cele mai multe valori 1 (incepe numerotarea de la 1)
     */
    public static int p10(int[][] matrix, int m, int n) {
        int max = 0, poz = 0;
        for (int i = 0; i < m; i++) {
            int j = n - 1, count = 0;
            while (j >= 0 && matrix[i][j] == 1) {
                count++;
                j--;
            }
            if (count > max) {
                poz = i;
                max = count;
            }
        }
        return poz + 1;

    }

    /**
     * genereaza toate numerele cuprinse intre 1 si n.
     *
     * @param n: valoarea maxima a nr generate
     */
    public static void p8(int n) {
        for (int i = 1; i <= n; i++) {
            String bin = "";
            int num = i;
            while (num > 0) {
                bin = (num % 2) + bin;
                num = num / 2;
            }
            System.out.println(bin);
        }
    }

    /**
     * determina suma elementelor din sub-matricile identificate de perechile date
     *
     * @param matrix: matricea in care calculam sumele
     * @param m:      numarul de linii
     * @param n:      numarul de coloane
     * @param list:   lista de perechi de coordonate
     */
    public static void p9(int[][] matrix, int m, int n, List<List<Integer>> list) {
        for (var l : list) {
            int mini, minj, maxi, maxj, sum = 0;
            if (l.get(0) > l.get(2)) {
                maxi = l.get(0);
                mini = l.get(2);
            } else {
                maxi = l.get(2);
                mini = l.get(0);
            }
            if (l.get(1) > l.get(3)) {
                maxj = l.get(1);
                minj = l.get(3);
            } else {
                maxj = l.get(3);
                minj = l.get(1);
            }

            for (int i = mini; i <= maxi; i++) {
                for (int j = minj; j <= maxj; j++) {
                    sum += matrix[i][j];
                }
            }
            System.out.println(sum);

        }


    }

    /**
     * marcheaza valori ce trebuie inlocuite
     *
     * @param matrix: matricea initiala
     * @param m:      numarul de linii
     * @param n:      numarul de coloane
     * @param x:      una din coordonatele unei valori din matrice
     * @param y:      cea de a doua coordonata a unei valori din matrice
     */
    public static void umple(int[][] matrix, int m, int n, int x, int y) {
        int[] dx = {0, 0, -1, 1};
        int[] dy = {-1, 1, 0, 0};
        Queue<Integer> q = new LinkedList<>();
        matrix[x][y] = 2;
        q.add(x);
        q.add(y);
        while (!q.isEmpty()) {
            int x2 = q.remove(), y2 = q.remove();
            matrix[x2][y2] = 2;
            for (int i = 0; i < 4; i++) {
                int x3 = x2 + dx[i];
                int y3 = y2 + dy[i];
                if (x3 < m && y3 < n && x3 >= 0 && y3 >= 0 && matrix[x3][y3] == 0) {
                    q.add(x3);
                    q.add(y3);
                }
            }

        }
    }

    /**
     * inlocuieste cu 1 toate aparitiile elementelor egale cu 0, complet inconjurate de 1
     * (insulele de 0)
     *
     * @param matrix: matricea initiala
     * @param m:      numarul de linii
     * @param n:      numarul de coloane
     */
    public static void p11(int[][] matrix, int m, int n) {
        for (int i = 0; i < m; i++) {
            if (matrix[i][0] == 0) {
                umple(matrix, m, n, i, 0);
            }
            if (matrix[i][n - 1] == 0) {
                umple(matrix, m, n, i, n - 1);
            }
        }
        for (int j = 0; j < n; j++) {
            if (matrix[0][j] == 0) {
                umple(matrix, m, n, 0, j);
            }
            if (matrix[m - 1][j] == 0) {
                umple(matrix, m, n, m - 1, j);
            }
        }

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (matrix[i][j] == 0) matrix[i][j] = 1;
                else if (matrix[i][j] == 2) matrix[i][j] = 0;
                System.out.print(matrix[i][j]);
                System.out.print(" ");
                ;
            }
            System.out.println();
        }
    }


    public static void main(String[] args) {
        while (true) {
            Scanner in = new Scanner(System.in);
            System.out.println("Problema: ");
            int opt = in.nextInt();
            if (opt == 1) {
                String prop1 = "Ana are mere rosii si galbene";
                System.out.print("Caz mediu: ");
                System.out.println(p1(prop1));
                String prop2 = "a b c";
                System.out.print("Caz usor: ");
                System.out.println(p1(prop2));
                String prop3 = "ana a avut aalbine";
                System.out.print("Caz greu: ");
                System.out.println(p1(prop3));

            } else if (opt == 2) {
                List<Integer> loc3 = new ArrayList<Integer>();
                loc3.add(1);
                loc3.add(1);
                List<Integer> loc4 = new ArrayList<>();
                loc4.add(0);
                loc4.add(0);
                System.out.print("Caz mediu: ");
                System.out.println(p2(loc3, loc4));

                List<Integer> loc1 = new ArrayList<Integer>();
                loc1.add(1);
                loc1.add(5);
                List<Integer> loc2 = new ArrayList<>();
                loc2.add(4);
                loc2.add(1);
                System.out.print("Caz usor: ");
                System.out.println(p2(loc1, loc2));

                List<Integer> loc5 = new ArrayList<Integer>();
                loc5.add(3);
                loc5.add(10);
                List<Integer> loc6 = new ArrayList<>();
                loc6.add(11);
                loc6.add(12);
                System.out.print("Caz greu: ");
                System.out.println(p2(loc5, loc6));

            } else if (opt == 3) {
                List<Integer> vect1 = new ArrayList<>();
                vect1.add(1);
                vect1.add(0);
                vect1.add(2);
                vect1.add(0);
                vect1.add(3);
                List<Integer> vect2 = new ArrayList<>();
                vect2.add(1);
                vect2.add(2);
                vect2.add(0);
                vect2.add(3);
                vect2.add(1);
                System.out.print("Caz mediu: ");
                System.out.println(p3(vect1, vect2));

                List<Integer> vect3 = new ArrayList<>();
                vect3.add(1);
                vect3.add(0);
                vect3.add(0);
                vect3.add(0);
                vect3.add(3);
                List<Integer> vect4 = new ArrayList<>();
                vect4.add(0);
                vect4.add(2);
                vect4.add(4);
                vect4.add(3);
                vect4.add(0);
                System.out.print("Caz usor: ");
                System.out.println(p3(vect3, vect4));

                List<Integer> vect5 = new ArrayList<>();
                vect5.add(3);
                vect5.add(0);
                vect5.add(3);
                vect5.add(0);
                vect5.add(3);
                List<Integer> vect6 = new ArrayList<>();
                vect6.add(3);
                vect6.add(0);
                vect6.add(3);
                vect6.add(0);
                vect6.add(3);
                System.out.print("Caz greu: ");
                System.out.println(p3(vect5, vect6));


            } else if (opt == 4) {
                String prop = "ana are ana are mere rosii ana";
                System.out.print("Caz mediu: ");
                p4(prop);

                String prop2 = "ana are mere rosii";
                System.out.print("Caz usor: ");
                p4(prop2);

                String prop3 = "ana are ana are ana";
                System.out.print("Caz greu: ");
                p4(prop3);
            } else if (opt == 5) {
                int n1 = 5;
                List<Integer> list1 = new ArrayList<>();
                list1.add(1);
                list1.add(2);
                list1.add(3);
                list1.add(4);
                list1.add(2);
                System.out.print("Caz usor: ");
                System.out.println(p5(n1, list1));
                int n2 = 6;
                List<Integer> list2 = new ArrayList<>();
                list2.add(1);
                list2.add(2);
                list2.add(1);
                list2.add(1);
                list2.add(3);
                list2.add(2);
                System.out.print("Caz mediu: ");
                System.out.println(p5(n2, list2));
                int n3 = 9;
                List<Integer> list3 = new ArrayList<>();
                list3.add(1);
                list3.add(2);
                list3.add(1);
                list3.add(1);
                list3.add(3);
                list3.add(3);
                list3.add(3);
                list3.add(3);
                list3.add(2);
                System.out.print("Caz greu: ");
                System.out.println(p5(n3, list3));
            } else if (opt == 6) {
                List<Integer> list = new ArrayList<>();
                list.add(2);
                list.add(8);
                list.add(7);
                list.add(2);
                list.add(2);
                list.add(5);
                list.add(2);
                list.add(3);
                list.add(1);
                list.add(2);
                list.add(2);
                System.out.print("Caz mediu: ");
                System.out.println(p6(list));
                List<Integer> list2 = new ArrayList<>();
                list2.add(8);
                list2.add(8);
                list2.add(8);
                list2.add(8);
                list2.add(8);
                list2.add(8);
                System.out.print("Caz usor: ");
                System.out.println(p6(list2));
                List<Integer> list3 = new ArrayList<>();
                list3.add(7);
                list3.add(7);
                list3.add(7);
                list3.add(7);
                list3.add(8);
                list3.add(8);
                list3.add(8);
                System.out.print("Caz greu: ");
                System.out.println(p6(list3));
            } else if (opt == 7) {
                int k = 2;
                List<Integer> list = new ArrayList<>();
                list.add(7);
                list.add(4);
                list.add(6);
                list.add(3);
                list.add(9);
                list.add(1);
                System.out.print("Caz mediu: ");
                System.out.println(p7(list, k));
                int k2 = 2;
                List<Integer> list2 = new ArrayList<>();
                list2.add(7);
                list2.add(7);
                list2.add(7);
                list2.add(3);
                list2.add(9);
                list2.add(1);
                System.out.print("Caz greu: ");
                System.out.println(p7(list2, k2));
                int k3 = 2;
                List<Integer> list3 = new ArrayList<>();
                list3.add(1);
                list3.add(2);
                list3.add(3);
                list3.add(4);
                list3.add(5);
                list3.add(8);
                System.out.print("Caz usor: ");
                System.out.println(p7(list3, k3));
            } else if (opt == 8) {
                int n = 4;
                System.out.print("Caz mediu: ");
                p8(n);
                int n2 = 0;
                System.out.print("Caz usor: ");
                p8(n2);
                int n3 = 15;
                System.out.print("Caz greu: ");
                p8(n3);

            } else if (opt == 9) {
                int m = 5, n = 5;
                int[][] matrix = {
                        {0, 2, 5, 4, 1},
                        {4, 8, 2, 3, 7},
                        {6, 3, 4, 6, 2},
                        {7, 3, 1, 8, 3},
                        {1, 5, 7, 9, 4}
                };
                List<List<Integer>> list = new ArrayList<>();
                List<Integer> coord1 = new ArrayList<>();
                coord1.add(1);
                coord1.add(1);
                coord1.add(3);
                coord1.add(3);
                List<Integer> coord2 = new ArrayList<>();
                coord2.add(2);
                coord2.add(2);
                coord2.add(4);
                coord2.add(4);
                list.add(coord1);
                list.add(coord2);
                System.out.print("Caz mediu: ");
                p9(matrix, m, n, list);

                List<List<Integer>> list2 = new ArrayList<>();
                List<Integer> coord3 = new ArrayList<>();
                coord3.add(0);
                coord3.add(0);
                coord3.add(2);
                coord3.add(3);
                List<Integer> coord4 = new ArrayList<>();
                coord4.add(1);
                coord4.add(3);
                coord4.add(2);
                coord4.add(4);
                list2.add(coord3);
                list2.add(coord4);
                System.out.print("Caz greu: ");
                p9(matrix, m, n, list2);

                List<List<Integer>> list3 = new ArrayList<>();
                List<Integer> coord5 = new ArrayList<>();
                coord5.add(1);
                coord5.add(1);
                coord5.add(1);
                coord5.add(4);
                List<Integer> coord6 = new ArrayList<>();
                coord6.add(3);
                coord6.add(3);
                coord6.add(3);
                coord6.add(4);
                list3.add(coord5);
                list3.add(coord6);
                System.out.print("Caz usor: ");
                p9(matrix, m, n, list3);

            } else if (opt == 10) {
                int m = 3, n = 5;
                int[][] matrix = {
                        {0, 0, 0, 1, 1},
                        {0, 1, 1, 1, 1},
                        {0, 0, 1, 1, 1}
                };
                System.out.print("Caz mediu: ");
                System.out.println(p10(matrix, m, n));
                int[][] matrix2 = {
                        {1, 1, 1, 1, 1},
                        {0, 0, 0, 0, 0},
                        {0, 0, 0, 0, 0}
                };
                System.out.print("Caz usor: ");
                System.out.println(p10(matrix2, m, n));
                int[][] matrix3 = {
                        {0, 0, 0, 0, 1},
                        {0, 0, 0, 0, 0},
                        {0, 0, 0, 0, 0}
                };
                System.out.print("Caz greu: ");
                System.out.println(p10(matrix2, m, n));

            } else if (opt == 11) {
                int m = 8, n = 10;
                int[][] matrix = {
                        {1, 1, 1, 1, 0, 0, 1, 1, 0, 1},
                        {1, 0, 0, 1, 1, 0, 1, 1, 1, 1},
                        {1, 0, 0, 1, 1, 1, 1, 1, 1, 1},
                        {1, 1, 1, 1, 0, 0, 1, 1, 0, 1},
                        {1, 0, 0, 1, 1, 0, 1, 1, 0, 0},
                        {1, 1, 0, 1, 1, 0, 0, 1, 0, 1},
                        {1, 1, 1, 0, 1, 0, 1, 0, 0, 1},
                        {1, 1, 1, 0, 1, 1, 1, 1, 1, 1}
                };
                System.out.print("Caz greu: ");
                p11(matrix, m, n);
                int[][] matrix2 = {
                        {1, 1, 1, 1, 1, 1, 1, 1, 1, 1},
                        {1, 0, 1, 1, 1, 0, 1, 1, 1, 1},
                        {1, 1, 1, 1, 1, 1, 1, 1, 1, 1},
                        {1, 1, 1, 1, 1, 0, 1, 1, 0, 1},
                        {1, 1, 1, 1, 1, 1, 1, 1, 1, 1},
                        {1, 1, 1, 1, 1, 0, 1, 1, 1, 1},
                        {1, 1, 1, 1, 1, 1, 1, 1, 0, 1},
                        {1, 1, 1, 1, 1, 1, 1, 1, 1, 1}
                };
                System.out.print("Caz usor: ");
                p11(matrix2, m, n);
                int[][] matrix3 = {
                        {1, 1, 1, 1, 1, 1, 1, 1, 1, 1},
                        {1, 0, 0, 1, 1, 0, 1, 1, 1, 1},
                        {1, 0, 0, 1, 1, 1, 1, 1, 1, 1},
                        {1, 1, 1, 1, 1, 0, 1, 1, 0, 1},
                        {1, 0, 0, 1, 1, 0, 1, 1, 0, 0},
                        {1, 0, 0, 1, 1, 1, 0, 1, 0, 1},
                        {1, 1, 1, 0, 1, 1, 1, 0, 0, 1},
                        {1, 1, 1, 1, 1, 1, 1, 1, 1, 1}
                };
                System.out.print("Caz mediu: ");
                p11(matrix3, m, n);
            } else break;
        }
    }
}