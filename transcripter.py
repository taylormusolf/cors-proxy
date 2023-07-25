# import sys

# # We get the video ID from the command line arguments
# video_id = sys.argv[1]
# # video_id = 'iuFvq8zUC3A'

# outls = []

# tx = YouTubeTranscriptApi.get_transcript(video_id, languages=['en'])

# for i in tx:
#     outtxt = (i['text'])
#     outls.append(outtxt)

# # We join all the transcript lines into one big text block
# full_transcript = "\n".join(outls)

# # We print the transcript so it can be captured by the JS script
# print(full_transcript)


## working!
from youtube_transcript_api import YouTubeTranscriptApi
import sys
import warnings
warnings.filterwarnings("ignore")

video_id = sys.argv[1]
# video_id = 'Kw51fkRiKZU'
tx = YouTubeTranscriptApi.get_transcript(video_id, languages=['en'])
outls = []
for i in tx:
    outtxt = (i['text'])
    outls.append(outtxt)

full_transcript = " ".join(outls)

data_to_pass_back = full_transcript

output = data_to_pass_back
print(output)
# print(video_id)

sys.stdout.flush()



# import warnings
# warnings.filterwarnings("ignore")
# from youtube_transcript_api import YouTubeTranscriptApi
# # import sys
# # video_id = sys.argv[1]
# tx = YouTubeTranscriptApi.get_transcript('iuFvq8zUC3A', languages=['en'])
# outls = []
# for i in tx:
#     outtxt = (i['text'])
#     outls.append(outtxt)

# full_transcript = "\n".join(outls)

# data_to_pass_back = full_transcript

# output = data_to_pass_back
# print(output)
# # print(video_id)

# sys.stdout.flush()










# VERSION 2

# from youtube_transcript_api import YouTubeTranscriptApi
# import sys

# # We get the video ID from the command line arguments
# # video_id = sys.argv[1]
# video_id = 'iuFvq8zUC3A'

# outls = []

# tx = YouTubeTranscriptApi.get_transcript(video_id, languages=['en'])

# for i in tx:
#     outtxt = (i['text'])
#     outls.append(outtxt)

# # We join all the transcript lines into one big text block
# full_transcript = "\n".join(outls)

# # We print the transcript so it can be captured by the JS script
# print(full_transcript)



# VERSION 1


# from youtube_transcript_api import YouTubeTranscriptApi

# # def my_function(youtubeId):

# outls = []

# tx = YouTubeTranscriptApi.get_transcript('iuFvq8zUC3A', languages=['en'])

# for i in tx:
#     outtxt = (i['text'])
#     outls.append(outtxt)

#     with open("op.txt", "a") as opf:
#         opf.write(outtxt + "\n")