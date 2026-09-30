# Week 01 Engineering Journal

## What I learned

This week I learned that using AI for engineering work is not only about getting an answer. I also need to verify important technical claims before accepting them. I practiced the A-E-V-R approach and learned how to compare AI-generated answers with reference material.

I also learned more about scan-based DFT, including scan insertion, scan flip-flops, scan input (SI), and scan enable (SE). The AI comparison activity helped me understand the same DFT concept from two different explanations.

## What still confuses me

I still want to understand some of the deeper implementation details of scan insertion, especially how scan insertion is performed in an actual EDA tool flow and how scan-related constraints can affect timing and physical implementation.

I also want to become more confident in distinguishing basic DFT concepts from tool-specific implementation details.

## One AI output I initially trusted

I initially trusted the explanations given by Gemini and Claude about scan insertion because both answers were technically consistent and clearly explained the concept.

In particular, I initially accepted the explanations of the scan flip-flop, the MUX-based selection between functional data and scan data, and the role of the scan enable (SE) signal.

## How I verified it

I asked both Gemini and Claude the same VLSI/DFT question and compared their answers.

I then checked the main technical claims against the reference material used for the activity. The common explanation of scan insertion, scan flip-flops, SI, SE, and functional/scan selection was supported.

I also noticed that some additional claims, such as ATPG, timing and area overhead, and scan-enable buffering, required more evidence than the reference material provided. I therefore treated those claims cautiously instead of automatically accepting them.

## What the AI did well

AI was useful for explaining technical concepts in a structured way and for providing different levels of detail.

Using two AI assistants also helped me compare explanations of the same DFT topic. AI was especially useful for brainstorming, breaking down concepts, and identifying technical points that I could investigate further.

## What the AI could not be trusted to decide

AI could not be trusted to decide whether every technical claim was correct simply because the explanation sounded convincing.

For engineering work, I still need to check important claims against reliable references and use my own judgment. AI should not be the final authority for tool-specific commands, implementation details, timing claims, or other technical decisions that require verification.

## One question I still have

How does a real EDA tool perform scan insertion and scan-chain stitching on a synthesized VLSI design, and what checks are performed after scan insertion?

## What I will do differently next week

Next week I will verify important AI-generated technical claims earlier instead of accepting an answer first and checking it later.

I will continue using this workflow:

**Ask → Compare → Verify → Identify unsupported claims → Conclude → Document**

This will help me use AI more responsibly in my VLSI and engineering work.
