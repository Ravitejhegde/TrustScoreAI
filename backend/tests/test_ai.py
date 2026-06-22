from engines.model_analysis.ai_detector import analyze_ai_probability

sample = {

"ela":{

"ela_score":45

},

"noise":{

"noise_score":10

},

"lighting":{

"lighting_score":20

},

"clone":{

"clone_score":15

},

"texture":{

"texture_score":20

},

"background":{

"background_score":20

},

"anatomy":{

"anatomy_score":0

}

}

result = analyze_ai_probability(

sample

)

print(

result

)