# Automating Windows Display Settings

This readme only provides some of the context of the code, and cloning this repo and running it yourself can cause unintended consequences as it **will click on hardcoded coordinates on your screen**. If you want to apply this yourself I highly recommend to read my blog post [here](https://dev.to/juanjosada/automating-windows-display-settings-1c6f) first to understand what's going on, and how to adapt it to your own system.

---

## Intro
Recently I found out about the wonders of the PyAutoGUI library through the book 'Automate the Boring Stuff with Python' by Al Sweigart, which you can read online for free [here](https://automatetheboringstuff.com/). However, to actually learn something you have to apply it yourself, so I could think of no better thing to automate than one of the most tedious problems I'm sure everyone can relate to. Yes, you guessed it, it's **disabling one of your multiple monitors on your computer so you can use it for another input device** (in my case, an xbox).

---

## Context
So in case it wasn't clear due to my poor writing, this is probably a very niche solution to very niche problem, but what's fun about being an engineer if you can't use your skills to build tools that help you in your daily workflow? Even if you have to use them for years to make up for the time you spent developing them.

I have 3 monitors in my computer setup.

Usually all 3 monitors are used by my PC at the same time, however, I also use monitor 1 for my Xbox. My PC is connected to the monitor via a Display Port cable, while the Xbox uses an HDMI. The issue becomes that if I simply switch the input from DP to HDMI when playing xbox, the PC display remains active, but it's running in the 'background' for the PC. This means that when I move windows around, or open new windows, the 1st display is still fair game, which can make it impossible to keep track of things, as all I see in the main screen is the Xbox interface.

---

## The Idea
Every time I wanted to play xbox, I would open display settings and disable the first monitor, allowing the other two monitors act as the only ones available, therefore allowing me to use the first monitor for the Xbox freely, without fear of 'losing' any windows in a display that isn't actually being shown by the monitor.
Now, this is a pretty straightforward process, which only takes about 20 seconds to disable the monitor, and then another 20 to reenable it. That's 40 wasted seconds every time I play and stop playing, which can add up specially if you play often. So why not automate it?

Now, the automations are simple, one to disable the first monitor on my PC when I'm going to start playing Xbox, and another to reenable it after I'm done playing Xbox.