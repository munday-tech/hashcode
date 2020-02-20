from operator import itemgetter

filenames = ['d_tough_choices.txt']

class book():

    def __init__(self):
        self.scanned = {}
        self.idx = 0
        self.next_signup = 0

    def signup(self, library, current_day):

        library_totals = library[0].split()
        library_books = library[1].split()

        next_signup = current_day + int(library_totals[1]) - 1
        

        self.scanned[self.idx] = {'books': library_books,
                                    'day_of_scan': next_signup,
                                    'books_per_day': int(library_totals[2]),
                                    'scanned': []}

        self.idx += 1

        self.next_signup = next_signup

    def scan(self, library, books):
        pass


    def main(self):
        for file in filenames:
            with open(file, 'r') as f:
                
                totals = f.readline().strip().split(' ')

                scores = f.readline().strip().split(' ')

                self.library = [line.strip() for line in f.readlines()]

            library_order = []

            library_index = 0


            scanned = []
            # Choose best library order


            for idx, row in enumerate(self.library):
                if idx % 2 != 0:
                    continue

                if row:

                    days = int(row.split()[1])
            
                    total_days = (int(totals[2]) - sum([x[2] for x in library_order]))

                    total_books = len(self.library[idx + 1].split())
                    total = total_days * int(self.library[idx].split()[2])

                    if total <= total_books:
                        total_books = total

                    sum_score = 0

                    for i in range(total_books):
                        sum_score += int(scores[i])

                    library_order.append((library_index, idx, days, sum_score))

                    library_index += 1

                    library_order = sorted(library_order,key=itemgetter(2, 3))


            lib_for_result = library_order[:]

            count = 0
            for i in range(int(totals[2])):
                
                day = i
                print(day)
                if i == self.next_signup and library_order:
                    self.signup((self.library[library_order[0][1]], self.library[library_order[0][1] + 1]), i)

                    del library_order[0]


                for key in self.scanned.keys():
                    if day >= self.scanned[key]['day_of_scan']:
                        if self.scanned[key]['books']:
                            for i in range(int(self.scanned[key]['books_per_day'])):
                                if len(self.scanned[key]['books']) > 0:
                                    while True:
                                        if self.scanned[key]['books'][-1:] in scanned:
                                            del self.scanned[key]['books'][-1:]
                                        else:                                           
                                            scan = self.scanned[key]['books'].pop()
                                            scanned.append(scan)
                                            count += 1
                                            self.scanned[key]['scanned'].append(scan)
                                            break
            print(count)


            with open("d_output.txt", 'w') as output:
                output.write(f"{self.idx - 1}")

                for idx, lib in enumerate(lib_for_result):
                
                    try:
                        output.write('\n' + f"{str(lib[0])} {str(len(self.scanned[idx]['scanned']))}" + '\n')
                        output.write(f"{' '.join(self.scanned[idx]['scanned'])}")
                    except:
                        pass

                   

    
b = book()

b.main()
