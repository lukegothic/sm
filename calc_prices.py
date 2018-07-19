# products
base_categories = [
    "cat1", "cat2", "cat3"
]
base_normalizedproducts = [
    "np1": {
        "category": "cat1",
        "priceunits": "kg"
    }
]
base_brandedproducts = [
    "bp1": {
        "product": "np1"
    }
    "bp2": {
        "product": "np1"
    }
]
base_normalizedmarkets = [
    "nm1", "nm2", "nm3"
]
base_realmarkets = [
    "m1": {
        "nm": "nm1",
        "location": "lng,lat"
    }
]
marketxproduct = [
    { "m": "m1", "p": "bp1", "price": 11, "discount": 0.25 },
    { "m": "m1", "p": "bp2", "price": 2, "discount": None }
]
exceptions = {
    "nm1": "*",
    "nm2": {
        "c": ["cat1"],
        "p": ["bp2", "bp1"]
    }
}
import itertools
def pricesum(productcombination):
    total = 0
    for p in products:
        total += market_prices[productcombination[p]][p]
    return total

market_prices = {
    "m1": {
        "p1": 1,
        "p2": 2,
        "p3": 3,
        "p4": 4,
        "p5": 5
    },
    "m2": {
        "p1": 1.2,
        "p2": 1.5,
        "p3": 3.1,
        "p4": 4.1,
        "p5": 4.9
    },
    "m3": {
        "p1": 0.9,
        "p2": 2.1,
        "p3": 2.9,
        "p4": 4.2,
        "p5": 4.7
    },
    "m4": {
        "p1": 1.1,
        "p2": 2.2,
        "p3": 2.8,
        "p4": 3.5,
        "p5": 5.5
    },
    "m5": {
        "p1": 1.3,
        "p2": 2,
        "p3": 2.7,
        "p4": 3.8,
        "p5": 5.1
    }
}

markets = ["m1","m2","m3","m4","m5"]
products = ["p1","p2","p3","p4","p5"]

price_guide = []
for i in range(1, len(markets) + 1):
    nlevelpriceguide = []
    marketcombinations = itertools.combinations(markets, i)
    for mc in marketcombinations:
        productcombination = {}
        for p in products:
            pmin = float("inf")
            mmin = None
            for m in mc:
                if market_prices[m][p] < pmin:
                    pmin = market_prices[m][p]
                    mmin = m
            productcombination[p] = mmin
        nlevelpriceguide.append(productcombination)
    price_guide.append(nlevelpriceguide)

#print(price_guide)

for n in range(len(price_guide)):
    price_guide[n] = sorted(price_guide[n], key=pricesum)

for n in range(len(price_guide)):
    print("{} DIFERENTES".format(n + 1))
    for comb in price_guide[n]:
        print(comb)
        print(pricesum(comb))

# with open("prices.csv") as f:
#     markets_csv = f.readlines()
#
# markets = []
# for market in markets_csv:
#     markets.append(list((float)(m) for m in market.replace("\n", "").replace(",", ".").split(";")))
#
# print(markets)
#
# priceguide = []
# for i in range(1, len(markets) + 1):
#     print("Combinando {}".format(i))
#     marketcombinations = itertools.combinations(markets, i)
#     nlevelpriceguide = []
#     for mc in marketcombinations:
#         #print(mc)
#         for product in products:
#
#     #priceguide.append(nlevelpriceguide)
