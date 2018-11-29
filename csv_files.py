import csv
raw=[]
fields=[]
with open('SL_SRTS_ analysis.csv','r') as csv_file:
        csv_reader=csv.DictReader(csv_file)
        field = csv_reader.next()
        print(field)
        for line in csv_reader:
            raw.append(line)
            print(raw)


            print(line['Feature name'])







        # with open('newfile.csv','w') as newfile:
        #
        #     csv_writer=csv.writer(newfile)
        #
        #
        #
        #     for line in csv_reader:
        #         csv_writer.writerow(line)
                #
