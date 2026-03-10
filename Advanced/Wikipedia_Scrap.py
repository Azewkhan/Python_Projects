import wikipedia as wiki

#To look for related keywords for the given word
print(wiki.search("Computer"))

#Suggest the closest word for the incomplete word or misspelled
print(wiki.suggest("Compute"))

#Provides Summary
print(wiki.summary("Donald Trump"))

# Sets Different Language
wiki.set_lang("Fr")

#Save it as a Page to get different functionality

Page= wiki.page("Narendra Modi")
Page.content # Mainly gives summary
Page.url # Url for the Wiki page
Page.title # Title of the Wiki page
Page.images # Link for all the images in the article
