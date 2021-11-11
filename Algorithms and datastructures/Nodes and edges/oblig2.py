from collections import defaultdict
from heapq import heappush, heappop

class Graph:
    def __init__(self):
        #nmid = skuespillerid
        #ttid = filmid

        #ttid -> set(nmid)
        self._tt_graph = dict()

        #nmid -> set(ttid)
        self._nm_graph = defaultdict(set)

        #nmid -> name
        self._names = dict()

        #ttid -> tuple(tittel, rating)
        self._film_info = dict()

    def legg_til_kanter_nm(self, key: str, name: str, tt_ids: set[str]):
        known = lambda x: x in self._tt_graph
        self._nm_graph[key] = self._nm_graph[key].union(filter(known, tt_ids))
        for tt_id in filter(known, tt_ids):
            self._tt_graph[tt_id].add(key)
        self._names[key] = name

    def legg_til_filmer(self, key: str, tittel: str, rating: float):
        self._tt_graph[key] = set()
        self._film_info[key] = (tittel, rating)

    def antall_noder(self):
        return len(self._nm_graph)

    def antall_kanter(self):
        return int(sum(map(lambda x: len(x)*(len(x)-1)/2, self._tt_graph.values())))

    def komponenter(self):
        not_visitet = set(self._nm_graph.keys())
        results = defaultdict(lambda: 0)
        while not_visitet:
            waiting = set()
            waiting.add(not_visitet.pop())
            count = 1
            while waiting:
                skuespiller = waiting.pop()

                #itererer gjennom alle naboer
                for film in self._nm_graph[skuespiller]:
                    for nabo in self._tt_graph[film]:
                        if nabo in not_visitet:
                            count += 1
                            not_visitet.discard(nabo)
                            waiting.add(nabo)
            results[count] += 1
        return results



    # oppgave 2
    def six_degrees(self, startnode, sluttnode):
        """Finner korteste avstand mellom to noder med BFS

        Args:
            startnode, noden der soeket begynner
            sluttnode, finner korteste vei hit
        Returns:
            Returnerer fin string av sti fra startnode til sluttnode
        """
        ko = Ko() # ko av de neste nodene som skal gjennomsoekes i BFS
        ko.leggTil(startnode)
        besokt = {startnode} # besokte noder
        # HashMap {nokkel er node : verdien er mornode}
        sti = {} # sti fra startnode til sluttnode
        sti[startnode] = ""

        while not ko.erTom():
            skuespiller = ko.hent()
            # itererer over naboene til skuespiller
            for film in self._nm_graph[skuespiller]:
                for nabo in self._tt_graph[film]:

                    if nabo not in besokt:
                        ko.leggTil(nabo)
                        besokt.add(nabo)
                        sti[nabo] = skuespiller # skuespiller er mor-node til nabo

                        if nabo == sluttnode:
                            # funnet sluttnoden, finn korteste sti
                            kortesteSti = []
                            node = sluttnode
                            mor = sti[sluttnode]
                            while node != startnode:
                                filmid = self._nm_graph[node].intersection(self._nm_graph[mor]).pop()
                                kortesteSti.insert(0, f"===[ {self._film_info[filmid][0]} ({self._film_info[filmid][1]}) ] ===> {self._names[node]}")
                                node = mor
                                mor = sti[mor]

                            kortesteSti.insert(0, self._names[startnode])

                            # lag en pen string som returneres
                            tekst = ""
                            for linje in kortesteSti:
                                tekst += linje + "\n"
                            return tekst


    def chilleste_vei(self, nm_id_1, nm_id_2):
        res = self.chill(nm_id_1, nm_id_2)
    
        nyAct = []
        nyDict = {}
        b = nm_id_2
        nyAct.append(b)

        while b:
            nyDict[b] = res[b][1]

            b = res[b][0]
            nyAct.append(b)

            if(b==nm_id_1):
                nyDict[b] = "ferdig"
                break

        nyAct.reverse()

        totRating = 0
        antall = 0
        out = ""

        for i in nyAct:
            if(nyDict[i] == "ferdig"):
                out+= f"\n{self._names[i]}"
                continue
            else:
                
                rating = float(self._film_info[nyDict[i]][1])
                totRating+= 10-rating
                antall+=1
                out += "\n === " + self._film_info[nyDict[i]][0] + " (" + str(rating) + ") ===> " + self._names[i]
        
        

        out += f"\nTotal Weight: {totRating:.1f}"
        return out




    def chill(self, nm_id_1, nm_id_2):
       
        parentsOgFilmen = {nm_id_1 : None}

        visited = set()
        
        Q = [(0, nm_id_1)]

        dist = defaultdict(lambda:float("inf"))
        dist[nm_id_1] = 0

        while (len(Q) != 0):
          
            v = heappop(Q)
            cost = v[0]

            if(v[1] in visited):
                continue
            visited.add(v[1])

            #hvis noden er den vi ser etter
            if(v[1]== nm_id_2):
                return parentsOgFilmen
            
            #går gjennom alle filmene skuespilleren har vært i. 
            for i in self._nm_graph[v[1]]:

                #finner cost
                nyCost = cost + 10-float(self._film_info[i][1])

                #siden vi har flere skuespillere som bruker samme film som kant 
                #vi går altså gjennom alle skuespillerene i filmen
                for j in self._tt_graph[i]:

                    #sjekker at skuespilleren ikke er samme som v[i]
                    if(j != v[1]):

                        if (nyCost < dist[j]):
                            dist[j]= nyCost
                            parentsOgFilmen[j] = (v[1], i)
                            
                            heappush(Q,(nyCost, j))


class Ko:
    # Brukes i bredde_forst_sok
    def __init__(self):
        self._ko = []

    def leggTil(self, x):
        """Adds element to end of queue
        Args:
            x, element to be added
        """
        self._ko.append(x)

    def hent(self):
        """Removes first element in queue by slicing
        Returns:
            Elementet som fjernes
        """
        return self._ko.pop(0)

    def erTom(self):
        """Checks if queue is empty

        Returns:
            True, if queue is empty
            False, if queue is not empty
        """
        return len(self._ko) == 0




if __name__ == "__main__":
    print("Oppgave 1")

    graph = Graph()
    with open("movies.tsv", "r", encoding="UTF-8") as movies:
        for line in movies:
            line_split = line.strip().split("\t")
            graph.legg_til_filmer(line_split[0], line_split[1], float(line_split[2]))


    with open("actors.tsv", "r", encoding="UTF-8") as actors:
        for line in actors:
            line_split = line.strip().split("\t")
            graph.legg_til_kanter_nm(line_split[0], line_split[1], set(line_split[2:]))

    print(f"Nodes: {graph.antall_noder()}")
    print(f"Edges: {graph.antall_kanter()}")


    print("\nOppgave 2")
    print(graph.six_degrees("nm0548088", "nm0529208"))
    print(graph.six_degrees("nm0529208", "nm2982413"))

    print("Oppgave 3")
    #chill funker for:

    # "nm0031483", "nm0931324"
    # "nm0000288", "nm0001401" Christian Bale Angelina Jolie
    #"nm4689420", "nm0000365"
    # "nm2255973", "nm0000460"
    #"nm0424060", "nm0000243"
    # "nm0860712", "nm0001131"
    #"nm0087456", "nm0000206"
    #"nm0087456", "nm0214531"
    #"nm0000206", "nm0121974" - tar jævlig lang tid tho
    #"nm0000206", "nm0001357"- tar også jævlig lang tid

    print(graph.chilleste_vei("nm2255973", "nm0000460"))
    print(graph.chilleste_vei("nm0424060", "nm0000243"))
    print(graph.chilleste_vei("nm4689420", "nm0000365"))
    print(graph.chilleste_vei("nm0000288", "nm0001401"))
    print(graph.chilleste_vei("nm0031483", "nm0931324"))




    print("\nOppgave 4")
    result = graph.komponenter()
    for key in result:
        print(f"There are {result[key]} components of size {key}")




    
