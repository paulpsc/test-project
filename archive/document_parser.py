import collections
from collections import defaultdict

def parse_document(document):
  print(document)
  # TODO(pschang): Using space as separater is not enough.
  newdoc = document.split(" ")
  print(len(newdoc))

  word_counts = defaultdict(int)
  for word in newdoc:
    #print(word)
    word_counts[word] += 1
  #pass

  # TODO: Sort dictionary by value.
  sorted_word_counts = sorted(word_counts.items(), key = lambda x:x[1], reverse=True )
  print( sorted_word_counts[:10] )


  # TODO: Select top 10 to print.

def main():
  documents = [
#    'dog eat dog',
    'WASHINGTON — The television is on. The phone is never far away. And President Trump is repeatedly calling allies such as members of Congress and conservative radio hosts, telling them privately that he will not give in on his demand for funding for a border wall. What the president who campaigned on his ability to cut deals has not done, nine days into a partial government shutdown over his signature campaign issue, is reach out to Democratic congressional leaders to strike one. Virtually alone in the West Wing since the shutdown began, Mr. Trump has instead taken to Twitter to excoriate Democrats, and highlight that he canceled his own vacation to his private club in Florida while lawmakers left the city. He has lamented the negativity of the news media coverage, which has included repeated airings of Mr. Trump’s declaration in the Oval Office a few weeks ago that he would not blame Democrats for a shutdown, according to people familiar with his thinking. Even as some lawmakers floated compromises on Sunday, Democrats prepared to pass a bill to fund the government as soon as they take control of the House on Thursday. Like the Democrats, Mr. Trump appears to have dug in. And the uncertainty over what he might sign threatens to indefinitely drag out a shutdown that has affected 800,000 federal workers and shuttered parts of nine cabinet-level departments. After Senator Lindsey Graham, Republican of South Carolina, met with Mr. Trump over lunch on Sunday, he said the president would not accept any deal without funding for the wall. But he remained optimistic that a compromise could be reached and encouraged both sides to come together. “At the end of the day, there’s a deal to be had,” he said on Sunday. “We need to start talking again.” Still, Mr. Graham said after the meeting that the president had not signed on to his potential compromise, which would provide wall funding in return for work permits for the young undocumented immigrants known as Dreamers. Democrats also have no interest in such a plan right now. And there were other signs of a lengthy shutdown fight from the White House: The president has a new acting chief of staff, Mick Mulvaney, who is not averse to government shutdowns, and some advisers see the timing of the fight as preferable to a year from now, when Democrats will be preparing for the first votes in the 2020 presidential primaries. Editors’ Picks Is Denaturalization the Next Front in the Trump Administration’s War on Immigration? 2018: The Year in Climate Change How Does a Writer Put a Drug Trip Into Words? The president is also concerned that if he makes a deal, his core political support will falter, and his voters will see him as inauthentic after he talked about a wall in rally after rally for three years. As Mr. Trump was poised to sign a compromise bill ushered through the Republican-controlled Congress that would have funded the government through February, conservative commentators berated him as “gutless,” and some hard-line House Republicans urged him to reconsider. He backed away from the bill soon after.'
  ]

  # Parse each document.
  for document in documents:
    parse_document(document)
  
if __name__ == '__main__':
  main()