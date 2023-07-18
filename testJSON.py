event = "Threshold Crossed: 1 out of the last 1 datapoints [99.59994442900812 (05/04/23 05:13:00)] was greater than the threshold (80.0) (minimum 1 datapoint for OK -> ALARM transition)."
event2 = "Threshold Crossed: 1 out of the last 1 datapoints [44.79021950541814 (05/04/23 01:33:00)] was not greater than the threshold (80.0) (minimum 1 datapoint for ALARM -> OK transition)."


test = event.find("was greater than the threshold (80.0)")

if test != -1:
	print("80%이상 사용량을 돌파 하였습니다.")
else:
	print("80% 이상 사용량에서 정상으로 돌아왔습니다.")