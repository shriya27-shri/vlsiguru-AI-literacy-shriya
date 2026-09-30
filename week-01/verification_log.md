# Week 01 Verification Log

| Date | Question / claim | AI tool | Claim checked | Verification source / experiment | Result |
|---|---|---|---|---|---|
| 2026-09-29 | What is scan insertion in scan-based DFT? | Gemini | Scan insertion replaces/implements functional flip-flops as scan-capable flip-flops and connects them into scan chains. | AI comparison activity and reference material reviewed for the scan-insertion concept. | Core claim supported. |
| 2026-09-29 | How does a scan flip-flop differ from a normal functional flip-flop? | Gemini | A scan flip-flop adds scan input (SI) and scan enable (SE), with a selection between functional and scan data. | AI comparison activity and reference material reviewed. | Core claim supported. |
| 2026-09-29 | What is the role of scan enable (SE)? | Gemini | SE selects between the functional D path and the scan SI path; low selects functional operation and high selects scan operation. | AI comparison activity and reference material reviewed. | Core claim supported. |
| 2026-09-30 | What is scan insertion? | Claude | Scan insertion replaces/implements functional flip-flops as scan flip-flops and stitches them into scan chains. | AI comparison activity and reference material reviewed. | Core claim supported. |
| 2026-09-30 | What are the main signals of a scan flip-flop? | Claude | A scan flip-flop uses functional data D, scan input SI, scan enable SE, clock, and output Q. | AI comparison activity and reference material reviewed. | Core claim supported. |
| 2026-10-01 | What additional details were provided by the AI tools? | Gemini and Claude | Both tools provided additional implementation and test-flow details beyond the core scan-insertion explanation. | Compared both AI answers with the available reference material. | Additional claims were treated cautiously when the reference did not independently establish them. |

## Notes

### What did the AI get right?

Both AI assistants gave broadly consistent explanations of the fundamental scan-insertion concept. They correctly described scan flip-flops, scan chains, the scan input (SI), and the role of scan enable (SE). They also explained the functional and scan data selection using a MUX-based structure.

### What did the AI get wrong or leave unsupported?

The main concepts were consistent with the reference material. However, some additional details such as ATPG, area and timing overhead, scan-enable buffering, and specific implementation considerations were not independently established by the reference material used in this activity. These claims were therefore not treated as automatically verified.

### What did I learn about verification?

I learned that an AI-generated technical explanation should not be accepted only because it sounds correct. I should compare answers from multiple AI tools, identify the important technical claims, check them against reliable reference material, and clearly distinguish verified information from additional or unsupported claims.

My verification workflow is:

**Ask → Compare → Verify → Identify unsupported claims → Conclude → Document**
