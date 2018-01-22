import sys
sys.path.append('/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages')
BulkTest = jv.bulk_write([
			DeleteMany({"prix":50}),
			InsertOne({"nom":"TestAjoutJeux","description":"TestDescription","prix":50,"categorie":["Action","Multijoueurs"],"auteur":"EA"})
])
