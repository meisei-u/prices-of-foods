def to_md(x):
    temp=x.replace(",","|").split("\n")
    temp=["|"+e+"|" for e in temp if e!=""]
    temp.insert(1,"|---|---|---|")
    temp.insert(0,"# 価格表")

    return "\n".join(temp)

with open("prices.csv","r",encoding="utf-8") as f:
    with  open("prices.md","w",encoding="utf-8") as fw:
        fw.write(to_md(f.read()))

