import requests

url = "https://big-five-personality-insights.p.rapidapi.com/api/big5"

payload = [
	{
		"id": "1",
		"language": "en",
		"text": "Imagination is more important than knowledge. Knowledge is limited. Imagination encircles the world. Try not to become a man of success, but rather try to become a man of value. The important thing is not to stop questioning. Curiosity has its own reason for existing."
	},
    {
        "id": "2",
        "language": "en",
        "text": "Knowing yourself is the beginning of all wisdom. Educating the mind without educating the heart is no education at all. We are what we repeatedly do. Excellence, then, is not an act, but a habit."
    },
    {
        "id": "3",
        "language": "en",
        "text": "When the spirits are low, when the day appears dark, when work becomes monotonous, when hope hardly seems worth having, just mount a bicycle and go out for a spin down the road, without thought on anything but the ride you are taking."
    },
    {
        "id": "4",
        "language": "en",
        "text": "Until you make the unconscious conscious, it will direct your life and you will call it fate. I am not what happened to me, I am what I choose to become. Your visions will become clear only when you can look into your own heart. Who looks outside, dreams; who looks inside, awakes."
    },
    {
        "id": "5",
        "language": "en",
        "text": "Imagination is a strong, restless faculty, which claims to be heard and exercised: are we to be quite deaf to her cry, and insensate to her struggles? Life appears to me too short to be spent in nursing animosity, or registering wrongs. I can live alone, if self-respect, and circumstances require me so to do."
    },
    {
        "id": "6",
        "language": "en",
        "text": "Man is a mystery: if you spend your entire life trying to puzzle it out, then do not say that you have wasted your time. I occupy myself with this mystery, because I want to be a man. I want to say to you, about myself, that I am a child of this age, a child of unfaith and skepticism, and probably (indeed I know it) shall remain so to the end of my life. How dreadfully has it tormented me (and torments me even now) this longing for faith, which is all the stronger for the proofs I have against it."
    },
    {
        "id": "7",
        "language": "en",
        "text": "There is nothing I would not do for those who are really my friends. I have no notion of loving people by halves; it is not my nature. I do not want people to be very agreeable, as it saves me the trouble of liking them a great deal. Life seems but a quick succession of busy nothings."
    },
    {
        "id": "8",
        "language": "en",
        "text": "The first and greatest victory is to conquer yourself; to be conquered by yourself is of all things most shameful and vile. I am the wisest man alive, for I know one thing, and that is that I know nothing. At the touch of love, everyone becomes a poet."
    },
    {
        "id": "9",
        "language": "en",
        "text": "We are going to die, and that makes us the lucky ones. Most people are never going to die because they are never going to be born. Faith is the great cop-out, the great excuse to evade the need to think and evaluate evidence. Faith is belief in spite of, even perhaps because of, the lack of evidence."
    },
    {
        "id": "10",
        "language": "en",
        "text": "Being entirely honest with oneself is a good exercise. The mind is like an iceberg; it floats with one-seventh of its bulk above water. Words have a magical power. They can either bring the greatest happiness or the deepest despair."
    },
    {
        "id": "11",
        "language": "en",
        "text": "If we introduce kids to these ideas at an age-appropriate time, you can get them to think about these issues before they are in a situation where they have to deal with them. I was flipping through images of reality television, where there were these young people competing for a million dollars... and then I saw footage from the Iraq war, and these two things began to fuse together in a very unsettling way."
    },
    {
        "id": "13",
      	"language": "en",
	"text": "I definitely prefer planning things far ahead as it gives me a sense control and security. However, it can feel like a waste of time if the plans goes sideways early on. I usually make decision based on logic and to the limits of my knowledge. However, when I have insufficient knowledge I have no problem going with my intuition."
    },
    {
        "id": "14",
        "language": "en",
        "text": "This above all: to thine own self be true. A fool thinks himself to be wise, but a wise man knows himself to be a fool. Love looks not with the eyes, but with the mind; and therefore is winged Cupid painted blind."
    },
    {
        "id": "15",
        "language": "en",
        "text": "I am only resolved to act in that manner, which will, in my own opinion, constitute my happiness, without reference to you, or to any person so wholly unconnected with me. How despicably have I acted!... I, who have prided myself on my discernment!... Till this moment I never knew myself."
    },
    {
        "id": "16",
        "language": "en",
        "text": "I wish the Ring had never come to me. I wish none of this had happened. It is useless to meet revenge with revenge: it will heal nothing. I feel that as long as the Shire lies behind, safe and comfortable, I shall find wandering more bearable."
    },
    {
        "id": "17",
        "language": "en",
        "text": "To be, or not to be: that is the question. Frailty, thy name is woman! Thus conscience does make cowards of us all."
    },
    {
        "id": "18",
        "language": "en",
        "text": "Everyone thinks I'm special ... All those people in the Leaky Cauldron, Professor Quirrell, Mr. Ollivander ... But I don't know anything about magic at all. I knew I could do it this time, because I'd already done it. Does that make sense? Be brave, Professor. Be brave like my mother ... Otherwise, you disgrace her. Otherwise, she died for nothing. Otherwise, the bowl will remain empty ... forever."
    },
    {
        "id": "19",
        "language": "en",
        "text": "Me? I'm dishonest, and a dishonest man you can always trust to be dishonest. Honestly. It's the honest ones you want to watch out for, because you can never predict when they're going to do something incredibly... stupid. It's not just a keel and a hull and a deck and sails, that's what a ship needs but what a ship is... what the Black Pearl really is... is freedom. The problem is not the problem. The problem is your attitude about the problem."
    },
    {
        "id": "20",
        "language": "en",
        "text": "I am no bird; and no net ensnares me: I am a free human being with an independent will. I care for myself. The more solitary, the more friendless, the more unsustained I am, the more I will respect myself. I would always rather be happy than dignified."
    },
    {
        "id": "21",
        "language": "en",
        "text": "I want to do something, right here, right now, to shame them, to make them accountable, to show the Capitol that whatever they do or force us to do, there is a part of every tribute they can't own. That Rue was more than a piece in their Games. And so am I. What I need is the dandelion in the spring. The bright yellow that means rebirth instead of destruction. The promise that life can go on, no matter how bad our losses. That it can be good again."
    },
    {
        "id": "22",
        "language": "en",
        "text": "I have reached the conclusion that, in order to come by money honestly, one must work and know how to earn it with hand or brain. Woe to those who lead idle lives. Idleness is a dreadful illness and must be cured in childhood. If it is not cured then, it can never be cured."
    },
    {
        "id": "23",
        "language": "en",
        "text": "Pain and suffering are always inevitable for a large intelligence and a deep heart. The really great men must, I think, have great sadness on earth. To go wrong in one's own way is better than to go right in someone else's. The man who has a conscience suffers whilst acknowledging his sin. That is his punishment—as well as prison."
    },
    {
        "id": "24",
        "language": "en",
        "text": "My name is Sherlock Holmes. It is my business to know what other people do not know. It has long been an axiom of mine that the little things are infinitely the most important. It is a capital mistake to theorize before you have all the evidence. It biases the judgment."
    },
    {
        "id": "25",
        "language": "en",
        "text": "You said you'd always be there for me! But you're not. And it's because of me. It's my fault. I finally got some sense knocked into me. And I've got the bump to prove it. I can't go back. What would it prove, anyway? It won't change anything. You can't change the past."
    }
]
headers = {
	"x-rapidapi-key": "28f49ce9d8msh544586063b68d83p1a4a57jsnd98eedb00de9",
	"x-rapidapi-host": "big-five-personality-insights.p.rapidapi.com",
	"Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())