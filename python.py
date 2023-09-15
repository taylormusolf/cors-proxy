from youtube_transcript_api import YouTubeTranscriptApi
import sys
tx = YouTubeTranscriptApi.get_transcript(sys.argv[1], languages=['en'])
outls = []
for i in tx:
    outtxt = (i['text'])
    outls.append(outtxt)

full_transcript = " ".join(outls)

data_to_pass_back = full_transcript
output = data_to_pass_back
print(output)
# print({'var1': sys.argv[1], 'number': 1})
sys.stdout.flush()