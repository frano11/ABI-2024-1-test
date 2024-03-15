import Bio.Entrez as ez 
ez.email = "c.knorr@cq-bildung.de"

print("==== First Example ====")
with ez.esearch(db="pubmed",term='"Hepatitis C NS5B"[title] AND inhibitor[title]') as query:
    record_pub = ez.read(query)

print(record_pub)
print(record_pub["IdList"])
print()

print("==== Second Example ====")
with ez.esearch(db="gene",term='"wnt pathway"[All]') as query:
    record_gene = ez.read(query)

print(record_gene)
print(record_gene["IdList"])
print()

print("==== Third Example ====")
with ez.esearch(db="genome",term="monkeypox[title]") as query:
    record_genome = ez.read(query)

print(record_genome)
print(record_genome["IdList"])
print()

print("==== Fourth Example ====")
with ez.esearch(db="pubmed",term="monkeypox[title] AND 2022[Publication Date]") as query:
    record_pub2 = ez.read(query)

print(record_pub2)
print(record_pub2["IdList"])
print()

print("==== Fifth Example ====")
with ez.esearch(db="protein",term='"Borna Virus"[all] AND (250[Sequence length] : 500[Sequence length])') as query:
    record_prot = ez.read(query)

print(record_prot)
print(record_prot["IdList"])
print()

print("==== Sixth Example ====")
with ez.esearch(db="biosample",term='"varicella-zoster virus"[title]') as query:
    record_sample = ez.read(query)

print(record_sample)
print(record_sample["IdList"])
print()

print("==== Seventh Example ====")
with ez.esearch(db="structure",term='"pyruvate kinase"[title] AND "electron microscopy"[EXPM]') as query:
    record_sample = ez.read(query)

print(record_sample)
print(record_sample["IdList"])
print()