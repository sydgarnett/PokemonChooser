import creator2

file=open("APC/PokemonListAllNames.txt","r")
d=13
m=9
y=98
n="Sydney Garnett"
create=creator2.Creator2(d,m,y,n)
lines=file.readlines()

print (create.FinalNum())
print(lines[create.FinalNum()-1])