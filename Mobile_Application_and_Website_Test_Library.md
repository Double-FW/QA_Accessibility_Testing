1. Colour Meaning Redundancy Test

Source:

Requirement
Any information or state conveyed through colour must also be conveyed through at least one additional visual and one programmatically available (non-visual) method.

User Experience Behaviour Supported
Users do not need to perceive colour to understand meaning. A user with colour blindness, low vision, or using a screen reader can still distinguish states (e.g. selected, error, active) through text, icons, structure, or spoken feedback. Meaning remains stable even under altered display conditions such as greyscale or high contrast modes.

2. Screen Reader Colour Meaning Announcement Test

Source:

Requirement
Where colour conveys meaning, that meaning must be exposed to and announced by assistive technologies.

User Experience Behaviour Supported
Screen reader users receive equivalent semantic information rather than losing context entirely. The interface behaves as a fully described system rather than a partially silent one.

3. Logical Content Order Test

Source:

Requirement
Content must be presented in a meaningful, logical sequence when navigated linearly by assistive technologies.

User Experience Behaviour Supported
Users navigating sequentially (e.g. screen reader swipe or keyboard navigation) experience content in an order that aligns with comprehension and task flow. The interface behaves predictably, without forcing users to mentally reconstruct meaning from disordered fragments.

4. Focus and Navigation Continuity Test (Implicit within Content Order)

Source:

Requirement
Focus movement must follow a logical progression, and interactive components (e.g. modals) must manage focus without loss or disorientation.

User Experience Behaviour Supported
Users maintain orientation while navigating. When entering or exiting components, they are not “lost” in the interface and can continue tasks without cognitive overhead or re-navigation.

5. UI Scaling and Zoom Enablement Test

Source:

Requirement
Users must be able to scale interface content (zoom or magnification) without restriction.

User Experience Behaviour Supported
Users with low vision or situational impairments (e.g. glare) can enlarge content to a usable size. The system respects user control rather than enforcing a fixed visual presentation.

6. Content Accessibility Under Zoom Test

Source:

Requirement
All content must remain accessible and operable when zoomed or magnified.

User Experience Behaviour Supported
Users who zoom do not encounter hidden, truncated, or inaccessible content. Interaction remains viable even when only part of the interface is visible.

7. Text Resizing and Reflow Test

Source:

Requirement
Text must resize according to user settings and reflow without loss of readability or functionality.

User Experience Behaviour Supported
Users can increase text size without horizontal scrolling, overlap, or layout breakage. Reading becomes easier without introducing new barriers.

8. Scroll and Layout Adaptation Test

Source:

Requirement
Resized content must support appropriate scrolling and layout adaptation.

User Experience Behaviour Supported
Users can navigate enlarged content naturally. The interface behaves fluidly rather than rigidly, supporting continuous reading and interaction.

9. Automated Contrast Compliance Test

Source:

Requirement
All foreground and background combinations must meet defined contrast thresholds when assessed by automated tools.

User Experience Behaviour Supported
Text and interface elements are visually distinguishable under standard conditions, supporting readability for users with reduced contrast sensitivity.

10. Manual Legibility Under Impairment Simulation Test

Source:

Requirement
Text must remain legible when visual clarity is reduced (e.g. blurred vision or reduced colour perception).

User Experience Behaviour Supported
Users experiencing real-world conditions (fatigue, glare, visual impairment) can still read and interpret content without strain or ambiguity.

11. Decorative Content Exclusion Test

Source:

Requirement
Decorative or non-meaningful elements must not be exposed to assistive technologies or receive focus.

User Experience Behaviour Supported
Assistive technology users are not burdened with irrelevant information. Navigation remains efficient, with only meaningful content presented.

12. Non-Interactive Content State Test

Source:

Requirement
If non-meaningful elements are exposed, they must be clearly identified as unavailable or non-interactive.

User Experience Behaviour Supported
Users do not attempt actions on elements that cannot respond. The interface avoids false affordances and reduces confusion.

13. Image Alternative Presence Test

Source:

Requirement
All images must include an alternative text attribute.

User Experience Behaviour Supported
Users who cannot see images still receive equivalent information, avoiding gaps in understanding.

14. Image Alternative Quality Test

Source:

Requirement
Editorially significant images must have meaningful, context-appropriate alternative text.

User Experience Behaviour Supported
Users receive useful, concise descriptions that support comprehension rather than redundant or misleading information.

15. Decorative Image Handling Test

Source:

Requirement
Decorative images must have empty alternatives or be otherwise excluded from announcement.

User Experience Behaviour Supported
Users are not distracted by unnecessary descriptions, maintaining focus on meaningful content.

16. Instruction Availability Test

Source:

Requirement
All forms and interactive elements must provide instructions explaining their purpose and use.

User Experience Behaviour Supported
Users understand how to interact with controls without guesswork, reducing errors and hesitation.

17. Instruction Clarity and Error Prevention Test

Source:

Requirement
Instructions must be clear enough to help users avoid and correct errors.

User Experience Behaviour Supported
Users can complete tasks confidently, with reduced cognitive load and fewer failed interactions.

18. Multimodal Instruction Delivery Test

Source:

Requirement
Instructions must be available in both visual and non-visual forms where needed.

User Experience Behaviour Supported
Users with different sensory capabilities (vision, hearing) can access guidance equally, ensuring inclusive interaction.

19. Colour Contrast Verification Test (Manual/Tool-Based)

Source:

Requirement
All visible text must meet minimum contrast thresholds when measured.

User Experience Behaviour Supported
Users can read text reliably across a range of visual conditions, including low vision and poor display environments.

20. Colour Independence Test (Achromatopsia Simulation)

Source:

Requirement
Content must remain understandable when colour is removed entirely.

User Experience Behaviour Supported
Users who cannot perceive colour still understand structure, meaning, and state without ambiguity.

21. Colour Usage Redundancy Test (Cross-check)

Source:

Requirement
Any use of colour to convey meaning must be supported by alternative indicators such as text, icons, or patterns.

User Experience Behaviour Supported
Users do not rely on colour perception alone, ensuring consistent interpretation across all user groups.

22. Flicker Frequency Compliance Test

Source:

Requirement
Content must not flicker or flash more than three times within any one-second period, unless mitigations such as warnings and user controls are provided.

User Experience Behaviour Supported
Users are protected from physical harm or discomfort such as seizures, dizziness, or nausea. The interface behaves safely under all visual conditions and does not impose involuntary sensory stress.

23. Flicker Opt-In and Alternative Content Test

Source:

Requirement
Where flicker is unavoidable, users must be warned in advance and given the ability to opt out or access a non-flickering alternative.

User Experience Behaviour Supported
Users retain control over exposure to potentially harmful content and can choose safer alternatives without losing access to information.

24. Dynamic Content Discoverability Test

Source:

Requirement
Dynamically added or updated content must be perceivable and discoverable by assistive technologies without requiring the user to search for it.

User Experience Behaviour Supported
Users become aware of updates (e.g. errors, confirmations, status changes) at the right moment, without missing critical information or needing to re-scan the interface.

25. Dynamic Content Focus Stability Test

Source:

Requirement
Changes to content must not unexpectedly shift user focus unless a genuine change of context occurs.

User Experience Behaviour Supported
Users maintain continuity of interaction and are not disoriented by sudden or unexplained movement of focus during tasks.

26. Context Change Focus Management Test

Source:

Requirement
When a change of context occurs (e.g. dialog, new page state), focus must move appropriately and return to the initiating element when the context is closed.

User Experience Behaviour Supported
Users clearly understand when they have entered or exited a new interaction context, maintaining orientation and control throughout.

27. Status Message Announcement Test

Source:

Requirement
Status messages must be announced to assistive technologies without requiring focus changes.

User Experience Behaviour Supported
Users receive timely feedback about system events without interruption to their workflow.

28. Status Message Timing and Persistence Test

Source:

Requirement
Temporary messages must remain visible long enough to be read and understood, based on content length.

User Experience Behaviour Supported
Users, including those with slower reading speeds or cognitive processing needs, can fully perceive transient information before it disappears.

29. Reduced Motion Preference Respect Test

Source:

Requirement
Motion and animation must respect user system preferences for reduced motion.

User Experience Behaviour Supported
Users sensitive to motion are not exposed to animations that could cause discomfort, distraction, or illness.

30. Motion Control Availability Test

Source:

Requirement
Users must be able to pause, stop, or prevent motion-based content such as autoplaying video.

User Experience Behaviour Supported
Users maintain control over moving content and can stabilise the interface to support reading and focus.

31. Autoplay Audio Interference Test

Source:

Requirement
Automatically playing media must not interfere with assistive technologies, particularly by producing unexpected audio.

User Experience Behaviour Supported
Users relying on audio (e.g. screen readers) are not disrupted or masked by competing sound sources.

32. Images of Text Detection Test

Source:

Requirement
Text content must not be presented as images except where unavoidable.

User Experience Behaviour Supported
Text remains adaptable—resizable, re-colourable, and readable by assistive technologies—ensuring flexibility for diverse user needs.

33. Image Text Scalability Test

Source:

Requirement
When text is enlarged or magnified, all textual content must scale cleanly without pixelation.

User Experience Behaviour Supported
Users can enlarge content without degradation, maintaining clarity and readability.

34. Styling Independence Test

Source:

Requirement
Content must remain readable and functional when styles (e.g. CSS) are removed or unsupported.

User Experience Behaviour Supported
Users on older devices, assistive technologies, or custom display settings can still access core content and complete tasks.

35. Core Content Availability Without Styling Test

Source:

Requirement
All essential information and functionality must be available regardless of visual presentation layers.

User Experience Behaviour Supported
The system behaves as content-first rather than style-dependent, ensuring resilience across environments.

36. Typography Line Length Readability Test

Source:

Requirement
Text line length must support comfortable reading without excessive scanning effort.

User Experience Behaviour Supported
Users can track lines of text easily, reducing cognitive load and improving comprehension.

37. Text Resize Integrity Test (200%)

Source:

Requirement
Text must remain fully visible and readable when resized up to at least 200%.

User Experience Behaviour Supported
Users who increase text size do not encounter clipping, overlap, or loss of information.

38. Text Spacing Override Test

Source:

Requirement
Content must remain usable when users adjust spacing (line height, letter spacing, word spacing, paragraph spacing).

User Experience Behaviour Supported
Users with reading difficulties can customise spacing to improve readability without breaking layout or meaning.

39. Screen Magnification Awareness Test

Source:

Requirement
Content must not rely on users seeing the full screen at once and must remain usable under magnification.

User Experience Behaviour Supported
Users navigating a zoomed or magnified viewport can still locate and interpret related content without confusion.

40. Media Metadata Presence Test

Source:

Requirement
Media must include metadata describing its properties and available alternatives.

User Experience Behaviour Supported
Users can understand media content before engaging with it and locate accessible alternatives such as captions or audio descriptions.

41. Page Metadata Validity Test

Source:

Requirement
Pages must pass validation checks and include correct structural metadata such as language.

User Experience Behaviour Supported
Assistive technologies can interpret content accurately, including pronunciation and structure.

42. Page Title Accuracy Test

Source:

Requirement
Each page must have a concise, descriptive title reflecting its content.

User Experience Behaviour Supported
Users can orient themselves quickly, particularly when navigating across multiple pages or using assistive technologies.

43. Page Zoom Capability Test

Source:

Requirement
Users must be able to zoom the page using standard gestures or controls.

User Experience Behaviour Supported
Users can adjust overall scale to meet visual needs without restriction.

44. Progressive Enhancement Baseline Test

Source:

Requirement
Core functionality must be available without reliance on advanced technologies such as CSS or JavaScript.

User Experience Behaviour Supported
Users with limited technology, connectivity, or disabled features can still complete primary tasks.

45. Progressive Resilience Under Constraints Test

Source:

Requirement
Core functionality must remain available under degraded conditions (e.g. low bandwidth, limited device capability).

User Experience Behaviour Supported
Users in constrained environments still achieve essential outcomes without failure.

46. Relative Sizing Implementation Test

Source:

Requirement
Layout and text sizing must use relative units to support scaling and adaptability.

User Experience Behaviour Supported
Interfaces adapt fluidly to user preferences and device contexts.

47. Progressive Functionality Fallback Test

Source:

Requirement
Where advanced functionality is unavailable, a fallback experience or explanation must be provided.

User Experience Behaviour Supported
Users are not blocked by unsupported features and can still proceed or understand limitations.

48. JavaScript Dependency Accessibility Test

Source:

Requirement
Content and functionality must remain accessible when JavaScript is disabled or unsupported.

User Experience Behaviour Supported
Users retain access regardless of technical constraints or personal settings.

49. Visible Focus Indicator Test

Source:

Requirement
All focusable elements must provide a clear, visible indication when focused.

User Experience Behaviour Supported
Users navigating via keyboard or assistive devices can track their position accurately.

50. Focus Indicator Contrast and Distinction Test

Source:

Requirement
Focus indicators must be visually distinct and meet contrast expectations.

User Experience Behaviour Supported
Focus states are easily perceivable and not confused with other visual elements.

51. Selected vs Focus State Differentiation Test

Source:

Requirement
Selected states must be visually distinct from focus states.

User Experience Behaviour Supported
Users can differentiate between current selection and navigation position, avoiding ambiguity.

52. Hidden Focusable Element Visibility Test

Source:

Requirement
Elements that are hidden but focusable must become visible when they receive focus.

User Experience Behaviour Supported
Users navigating via keyboard are not disoriented by invisible interactions and can perceive actionable elements.

53. Visual Formatting Independence Test

Source:

Requirement
Meaning must not rely solely on visual formatting such as size, position, or styling.

User Experience Behaviour Supported
Users who cannot perceive visual styling still understand structure, hierarchy, and meaning through alternative cues.

54. Non-Visual Equivalence for Visual Information Test

Source:

Requirement
All visually conveyed information must have equivalent non-visual representations.

User Experience Behaviour Supported
Users of assistive technologies receive complete and equivalent information, ensuring parity of understanding.

55. Actionable Element Distinguishability Test

Source:

Requirement
All actionable elements must be clearly distinguishable from non-actionable content through visual cues, conventions, and assistive technology semantics.

User Experience Behaviour Supported
Users can immediately recognise what is interactive versus static, reducing hesitation, cognitive load, and interaction errors.

56. Actionable Element Semantic Identification Test

Source:

Requirement
All actionable elements must expose correct roles, labels, and traits to assistive technologies.

User Experience Behaviour Supported
Users of assistive technologies can accurately identify controls, understand their purpose, and interact with them predictably.

57. Native Control Usage Test

Source:

Requirement
Native platform controls must be used wherever possible instead of custom elements lacking built-in semantics.

User Experience Behaviour Supported
Users benefit from familiar interaction patterns and consistent behaviour across applications and devices.

58. Actionable Element Interaction Expectation Test

Source:

Requirement
Controls must behave in line with user expectations based on their visual representation and common conventions.

User Experience Behaviour Supported
Users can predict outcomes of interactions, reducing confusion and increasing efficiency.

59. Adjustable Interaction Parameters Test

Source:

Requirement
Users must be able to adjust key interaction parameters such as volume, text size, colour, difficulty, and timing where applicable.

User Experience Behaviour Supported
Users can tailor the experience to their sensory, cognitive, and physical needs, enabling sustained and effective interaction.

60. Adjustable Control Complexity Test

Source:

Requirement
Interfaces must allow adjustment of interaction complexity, including simplifying controls and reducing the number of choices.

User Experience Behaviour Supported
Users with cognitive or motor challenges can engage without being overwhelmed or excluded by complexity.

61. Adjustable Input Precision Test

Source:

Requirement
Users must be able to adjust target sizes and input sensitivity for interactive elements.

User Experience Behaviour Supported
Users with limited dexterity or precision can successfully interact with controls without repeated errors.

62. Adjustable Pace and Timing Test

Source:

Requirement
Users must be able to control timing aspects such as timeouts, speed of interaction, and progression pace.

User Experience Behaviour Supported
Users can operate at a comfortable speed, avoiding pressure, mistakes, or exclusion due to time constraints.

63. Alternative Input Navigation Test

Source:

Requirement
All interactive elements must be navigable using alternative input methods such as keyboard, switch devices, or assistive technologies.

User Experience Behaviour Supported
Users are not restricted to a single input modality and can navigate interfaces using their preferred or required method.

64. Alternative Input Activation Test

Source:

Requirement
All controls must be operable via alternative input methods, not just navigable.

User Experience Behaviour Supported
Users can complete tasks independently without needing unsupported gestures or input types.

65. Gesture Independence Test

Source:

Requirement
Functionality triggered by gestures must have equivalent non-gesture alternatives.

User Experience Behaviour Supported
Users who cannot perform gestures (e.g. swipe, pinch) can still access the same functionality.

66. Multi-Input Interaction Consistency Test

Source:

Requirement
Interaction patterns must behave consistently across different input methods.

User Experience Behaviour Supported
Users experience predictable and coherent behaviour regardless of how they interact with the interface.

67. Media Caption Synchronisation Test

Source:

Requirement
Subtitles or captions must be synchronised with audio content.

User Experience Behaviour Supported
Users who cannot hear audio can follow content accurately in real time.

68. Audio Description Availability Test

Source:

Requirement
Visual information critical to understanding must be available via audio description or equivalent.

User Experience Behaviour Supported
Users who cannot see visual content receive complete narrative understanding.

69. Media Alternative Format Completeness Test

Source:

Requirement
All essential audio and visual information must be available in alternative formats such as captions, transcripts, or sign language.

User Experience Behaviour Supported
Users can access content regardless of sensory limitations or environmental constraints.

70. Non-Text Content Purpose Equivalence Test

Source:

Requirement
Alternative text must convey the purpose or intent of non-text content, not just describe its appearance.

User Experience Behaviour Supported
Users understand why content exists and what it does, rather than just what it looks like.

71. Functional Image Action Description Test

Source:

Requirement
Images used as controls must have alternatives that describe the action performed.

User Experience Behaviour Supported
Users can operate controls confidently without needing to see the visual icon.

72. Alternative Text Uniqueness Test

Source:

Requirement
Alternative text must be unique where multiple similar elements exist.

User Experience Behaviour Supported
Users can distinguish between similar controls or items without ambiguity.

73. Alternative Text Brevity and Clarity Test

Source:

Requirement
Alternative text must be concise, avoiding redundancy and unnecessary phrasing.

User Experience Behaviour Supported
Users receive efficient, clear information without cognitive overload.

74. Decorative Image Null Alternative Test

Source:

Requirement
Purely decorative images must have null (empty) alternative text.

User Experience Behaviour Supported
Users are not burdened with irrelevant information that adds noise to the experience.

75. Functional Image Comprehension Test

Source:

Requirement
Alternative text for functional images must enable full understanding of the control or content without visual reference.

User Experience Behaviour Supported
Users can complete tasks and interpret content equivalently to sighted users.

76. Alternative Text Language Consistency Test

Source:

Requirement
Alternative text must match the language of the surrounding content.

User Experience Behaviour Supported
Users experience coherent pronunciation and comprehension when using assistive technologies.

77. Alternative Text Non-Redundancy Test

Source:

Requirement
Alternative text must not duplicate adjacent visible text unless necessary.

User Experience Behaviour Supported
Users avoid repetitive information and maintain efficient navigation.

78. Multiple Interaction Method Availability Test

Source:

Requirement
All actionable elements must support multiple interaction methods (e.g. mouse, touch, keyboard, assistive technology).

User Experience Behaviour Supported
Users can choose the most suitable interaction method for their abilities and context.

79. Gesture Alternative Provision Test

Source:

Requirement
Gesture-based interactions must be supplemented with alternative controls.

User Experience Behaviour Supported
Users are not excluded due to inability to perform gestures.

80. Interaction Method Flexibility Test

Source:

Requirement
Interfaces must allow users to switch between interaction methods seamlessly.

User Experience Behaviour Supported
Users can adapt interaction styles dynamically based on context, ability, or preference.

81. Document Title Uniqueness and Clarity Test

Source:

Requirement
Each page must have a unique, descriptive, and concise title reflecting its purpose.

User Experience Behaviour Supported
Users can orient themselves quickly and differentiate between pages when navigating.

82. Heading Structure Hierarchy Test

Source:

Requirement
Headings must be logically structured and hierarchical.

User Experience Behaviour Supported
Users can scan, navigate, and understand content structure efficiently.

83. Landmark Region Identification Test

Source:

Requirement
Page regions must be defined using appropriate landmarks.

User Experience Behaviour Supported
Users can navigate quickly between major sections of a page.

84. Landmark Navigation Efficiency Test

Source:

Requirement
Landmarks must support efficient navigation and orientation.

User Experience Behaviour Supported
Users can move through content strategically rather than sequentially.

85. Main Content Identification Test

Source:

Requirement
A single, clearly defined main content area must be present.

User Experience Behaviour Supported
Users can quickly locate the primary purpose of the page.

86. Skip Navigation Mechanism Test

Source:

Requirement
Mechanisms must exist to skip repetitive navigation and reach main content directly.

User Experience Behaviour Supported
Users avoid unnecessary repetition and reach relevant content efficiently.

87. Landmark Labelling Clarity Test

Source:

Requirement
Landmarks must be clearly labelled where multiple similar regions exist.

User Experience Behaviour Supported
Users can distinguish between similar areas and navigate accurately.

88. Functional Image Alt Presence Test

Source:

Requirement
All images must have an alternative text attribute, even if empty for decorative images.

User Experience Behaviour Supported
Users are never left without context or clarity when encountering images.

89. Alternative Text Quality Test

Source:

Requirement
Alternative text must be grammatically correct, meaningful, and useful.

User Experience Behaviour Supported
Users receive high-quality information that supports comprehension and usability.

90. Interaction Trigger Timing Test

Source:

Requirement
Actions must only be triggered at the appropriate stage of user interaction (e.g. on release for touch, on activation for keyboard), not prematurely.

User Experience Behaviour Supported
Users can explore, adjust, or cancel interactions without unintended consequences, maintaining control and reducing accidental activation.

91. Touch Interaction Completion Test

Source:

Requirement
Touch-based interactions must not trigger actions at the start of contact, but only when the interaction is completed.

User Experience Behaviour Supported
Users can correct positioning before committing to an action, improving accuracy and confidence.

92. Keyboard Interaction Responsiveness Test

Source:

Requirement
Keyboard interactions must trigger actions at the appropriate point in the interaction model (e.g. key activation rather than release where expected).

User Experience Behaviour Supported
Users relying on keyboards experience predictable, efficient activation aligned with established interaction patterns.

93. Audio Non-Interference Test

Source:

Requirement
Audio content must not conflict with or obscure assistive technology output.

User Experience Behaviour Supported
Users can clearly perceive both system feedback and media content without cognitive overload or missed information.

94. Screen Reader Audio Priority Test

Source:

Requirement
Assistive technology audio must remain perceivable and not be masked by embedded media.

User Experience Behaviour Supported
Users retain continuous access to navigation and contextual information while interacting with media.

95. Background Image Meaning Equivalence Test

Source:

Requirement
Background images that convey meaning must have an equivalent accessible alternative provided through other means.

User Experience Behaviour Supported
Users who cannot perceive background images still receive all essential information and context.

96. Background Image Accessibility Exposure Test

Source:

Requirement
Meaningful imagery must be exposed to assistive technologies in a programmatically determinable way.

User Experience Behaviour Supported
Users can access, navigate, and understand visual content through assistive technologies.

97. Decorative Background Image Suppression Test

Source:

Requirement
Decorative images must not be exposed to assistive technologies.

User Experience Behaviour Supported
Users are not distracted by irrelevant or non-informative content.

98. Colour Independence Test

Source:

Requirement
Colour must not be the sole means of conveying information, state, or interaction.

User Experience Behaviour Supported
Users who cannot perceive colour can still understand content, status, and actions.

99. Non-Colour Indicator Presence Test

Source:

Requirement
Alternative indicators (such as icons or text) must supplement colour-based meaning.

User Experience Behaviour Supported
Users receive redundant cues that reinforce understanding across different perception abilities.

100. Focus Indicator Contrast Test

Source:

Requirement
Focus indicators must have sufficient contrast against surrounding content.

User Experience Behaviour Supported
Users can reliably track focus location during navigation, particularly when using keyboards or assistive tools.

101. Colour Contrast Compliance Test

Source:

Requirement
Text and background combinations must meet minimum contrast ratios (e.g. 4.5:1 for standard text).

User Experience Behaviour Supported
Users can read content comfortably across different lighting conditions and visual capabilities.

102. Link Differentiation Contrast Test

Source:

Requirement
Links must be distinguishable from surrounding text with sufficient contrast and not rely solely on colour.

User Experience Behaviour Supported
Users can easily identify interactive text elements within content.

103. Colour Perception Robustness Test

Source:

Requirement
Content must remain understandable under different colour perception conditions (e.g. colour blindness or altered displays).

User Experience Behaviour Supported
Users experience consistent meaning regardless of how colours are perceived.

104. State Communication Without Colour Test

Source:

Requirement
States such as errors, progress, or selection must be communicated without reliance on colour alone.

User Experience Behaviour Supported
Users can interpret system feedback clearly in all contexts.

105. Data Visualisation Non-Colour Encoding Test

Source:

Requirement
Charts and graphs must use additional visual encodings beyond colour to differentiate data.

User Experience Behaviour Supported
Users can interpret data accurately without relying on colour distinctions.

106. Link Visual Distinguishability Test

Source:

Requirement
Links within content must be visually distinguishable through styling beyond colour alone.

User Experience Behaviour Supported
Users can quickly identify navigational elements within text.

107. Interactive Element State Change Test

Source:

Requirement
Interactive elements must visibly change state on hover and focus.

User Experience Behaviour Supported
Users receive immediate feedback confirming interactivity and current focus.

108. Control Type Differentiation Test

Source:

Requirement
Different control types (e.g. links vs buttons) must be visually distinct.

User Experience Behaviour Supported
Users can infer behaviour and expected outcomes based on visual cues.

109. Automatic Page Refresh Prevention Test

Source:

Requirement
Pages must not refresh automatically without user awareness or control.

User Experience Behaviour Supported
Users maintain orientation and do not lose their place unexpectedly.

110. Content Stability During Navigation Test

Source:

Requirement
Content must not change or refresh unexpectedly during navigation or focus movement.

User Experience Behaviour Supported
Users can navigate reliably without disruption or disorientation.

111. Text Resize Visibility Test

Source:

Requirement
Content must remain visible and readable when text size is increased up to 200%.

User Experience Behaviour Supported
Users with low vision can read content without loss of information.

112. Text Resize Usability Test

Source:

Requirement
Interfaces must remain usable when text is resized, without overlap or loss of functionality.

User Experience Behaviour Supported
Users can interact with controls and complete tasks even at increased text sizes.

113. Zoom Support Test

Source:

Requirement
Interfaces must support zoom functionality or provide an equivalent method of scaling content.

User Experience Behaviour Supported
Users can enlarge content according to their needs without restriction.

114. Responsive Text Scaling Test

Source:

Requirement
Text must scale using responsive units that respect user and browser settings.

User Experience Behaviour Supported
Users experience consistent scaling behaviour across devices and settings.

115. Target Spacing Separation Test

Source:

Requirement
Actionable elements must have sufficient inactive space between them.

User Experience Behaviour Supported
Users can select targets accurately without accidentally activating adjacent controls.

116. Touch Target Size Test

Source:

Requirement
Interactive elements must meet minimum size requirements for touch interaction.

User Experience Behaviour Supported
Users can comfortably interact with controls without precision strain.

117. Target Overlap Prevention Test

Source:

Requirement
Interactive elements must not overlap or touch in a way that causes ambiguity.

User Experience Behaviour Supported
Users can clearly identify and activate intended controls without error.

118. Autoplay Prevention Test

Source:

Requirement
Audio or video content must not play automatically unless the user has been clearly informed in advance or is provided with immediate controls to stop, pause, or mute it.

User Experience Behaviour Supported
Users retain control over sensory input, avoiding disruption, distress, or interference with assistive technology.

119. Autoplay User Control Availability Test

Source:

Requirement
Where autoplay is present, fully accessible controls to pause, stop, or mute must be immediately available and operable.

User Experience Behaviour Supported
Users can quickly regain control over unexpected media playback.

120. Autoplay Opt-In and Persistence Test

Source:

Requirement
Autoplay must be opt-in, and user preferences regarding autoplay behaviour must persist across sessions.

User Experience Behaviour Supported
Users can define and maintain a consistent, predictable media experience aligned with their preferences.

121. Interaction Consistency Test

Source:

Requirement
Interface elements must behave consistently across screens, maintaining predictable patterns of interaction and navigation.

User Experience Behaviour Supported
Users can transfer learning across contexts, reducing cognitive load and improving efficiency.

122. Control Meaning Consistency Test

Source:

Requirement
Controls, icons, and labels must maintain consistent meaning across the interface and must not change interpretation between contexts.

User Experience Behaviour Supported
Users can trust that controls will behave as expected without re-learning their function.

123. Visual-to-Function Alignment Test

Source:

Requirement
The visual appearance of controls must accurately indicate their function and method of interaction.

User Experience Behaviour Supported
Users can infer how to interact with elements without trial-and-error.

124. Gesture Convention Support Test

Source:

Requirement
Common gesture patterns (e.g. swipe, drag) must be supported alongside alternative input methods.

User Experience Behaviour Supported
Users can interact using familiar patterns or alternative methods depending on ability and context.

125. Icon Text Equivalence Test

Source: and

Requirement
Icons must be accompanied by visible or programmatically available text that conveys their meaning.

User Experience Behaviour Supported
Users who cannot interpret icons receive equivalent information through text.

126. Decorative Icon Suppression Test

Source: and

Requirement
Icons that are decorative must be hidden from assistive technologies.

User Experience Behaviour Supported
Users are not burdened with redundant or meaningless announcements.

127. Icon Accessibility Name Test

Source:

Requirement
Interactive elements that rely on icons must have a clear accessible name derived from text or equivalent attributes.

User Experience Behaviour Supported
Users can understand and operate icon-based controls using assistive technologies.

128. Icon Font Avoidance Test

Source: and

Requirement
Icon fonts must not be used where they compromise accessibility; scalable vector graphics (SVG) should be preferred.

User Experience Behaviour Supported
Users do not experience loss of meaning due to font overrides or assistive technology misinterpretation.

129. Icon State Communication Test

Source:

Requirement
Icons representing state must update both visually and programmatically to reflect current status.

User Experience Behaviour Supported
Users receive accurate, real-time feedback about system state.

130. Video Control Accessibility Test

Source:

Requirement
Custom video controls must be accessible via keyboard and assistive technologies and must replicate native functionality.

User Experience Behaviour Supported
Users can control media playback regardless of input method or assistive technology use.

131. Video Caption Availability Test

Source:

Requirement
Videos with dialogue must provide captions, either enabled by default or accessible via controls.

User Experience Behaviour Supported
Users can access audio content through text equivalents.

132. Video Control Label Synchronisation Test

Source:

Requirement
Video control labels and icons must update dynamically to reflect current playback state.

User Experience Behaviour Supported
Users receive clear and consistent feedback about playback status.

133. Timeline Accessibility Test

Source:

Requirement
Media timelines must be keyboard operable and provide accessible value information.

User Experience Behaviour Supported
Users can navigate media content precisely and understand current position.

134. Input Device Adaptability Test

Source:

Requirement
Interactive systems must support multiple input methods and allow adaptation of control schemes.

User Experience Behaviour Supported
Users can interact using devices and configurations suited to their abilities.

135. Input Complexity Adjustment Test

Source:

Requirement
Systems must provide simplified interaction modes where complex controls exist.

User Experience Behaviour Supported
Users with motor or cognitive impairments can operate interfaces with reduced effort.

136. Input Sensitivity and Pace Adjustment Test

Source:

Requirement
Users must be able to adjust sensitivity, timing, or pace of interactions where applicable.

User Experience Behaviour Supported
Users can interact at a comfortable speed and precision level.

137. Input Device Parity Test

Source:

Requirement
All functionality available via pointer input must also be operable via keyboard.

User Experience Behaviour Supported
Users are not excluded based on input device limitations.

138. Form Label Presence Test

Source:

Requirement
All form controls must have a visible and programmatically associated label.

User Experience Behaviour Supported
Users understand what information is required and how to provide it.

139. Input Format Indication Test

Source:

Requirement
Expected input formats must be clearly indicated within labels or instructions.

User Experience Behaviour Supported
Users can enter data correctly without guesswork.

140. Input Method Appropriateness Test

Source:

Requirement
Form fields must invoke appropriate input methods (e.g. numeric keyboard for numbers).

User Experience Behaviour Supported
Users can input data efficiently with reduced cognitive and physical effort.

141. Gesture Alternative Input Test

Source:

Requirement
Gesture-based interactions must have accessible non-gesture alternatives.

User Experience Behaviour Supported
Users who cannot perform gestures can still complete tasks.

142. Keyboard Navigation Coverage Test

Source:

Requirement
All interactive elements must be reachable and operable using keyboard navigation.

User Experience Behaviour Supported
Users can fully interact with the interface without a mouse or touch input.

143. Focus Visibility Test

Source:

Requirement
Keyboard focus must be visually clear and consistently indicated.

User Experience Behaviour Supported
Users can track navigation position reliably.

144. Logical Focus Order Test

Source:

Requirement
Focus must move in a logical and predictable sequence.

User Experience Behaviour Supported
Users can navigate content in a meaningful order.

145. Keyboard Interaction Completeness Test

Source:

Requirement
All interactive components must be fully operable using standard keyboard interactions.

User Experience Behaviour Supported
Users can perform all tasks without alternative input devices.

146. Focus Return Behaviour Test

Source:

Requirement
Focus must return to the initiating element after temporary content (e.g. dialogs) is closed.

User Experience Behaviour Supported
Users maintain orientation within workflows.

147. Hidden Content Focus Reveal Test

Source:

Requirement
Content hidden visually must become visible when it receives keyboard focus.

User Experience Behaviour Supported
Users are aware of and can interact with all focusable elements.

148. Keyboard Trap Prevention Test

Source:

Requirement
Users must not become trapped within any interface element when navigating via keyboard.

User Experience Behaviour Supported
Users can freely navigate through and exit all interface components.

149. Focus Escape Mechanism Test

Source:

Requirement
Where complex components exist, a clear and operable method to exit must be provided.

User Experience Behaviour Supported
Users can recover from constrained interaction contexts.

150. Touch Target Minimum Size Test

Source:

Requirement
Touch targets must meet minimum physical size requirements (e.g. ~7mm).

User Experience Behaviour Supported
Users can accurately interact with controls using touch input.

151. Touch Target Expansion Strategy Test

Source:

Requirement
Where content is visually small, the interactive area must be expanded to meet usability requirements.

User Experience Behaviour Supported
Users can interact with small visual elements without precision difficulty.

152. Touch Target Grouping Test

Source:

Requirement
Related interactive elements should be grouped into larger unified touch targets where appropriate.

User Experience Behaviour Supported
Users benefit from simplified interaction and reduced error rates.

153. Focus Change Control Test

Source:

Requirement
Focus must not automatically change during user input unless explicitly triggered by the user.

User Experience Behaviour Supported
Users remain oriented and in control while entering or reviewing information, avoiding disorientation or interruption.

154. Input Activation Completion Test

Source:

Requirement
Actions must only be triggered after a user completes an interaction (e.g. releasing touch or confirming input), not during initial engagement.

User Experience Behaviour Supported
Users can adjust or cancel interactions before committing, reducing accidental actions.

155. Consistent Labelling Across Contexts Test

Source:

Requirement
Labels, headings, and textual identifiers must remain consistent across pages, platforms, and contexts.

User Experience Behaviour Supported
Users can recognise and understand elements without reinterpreting meaning in different contexts.

156. Repeated Element Function Consistency Test

Source:

Requirement
Elements used multiple times must perform the same function and have identical accessible representations.

User Experience Behaviour Supported
Users can rely on repeated patterns and behaviours without confusion.

157. Distinct Element Differentiation Test

Source:

Requirement
Elements that perform different functions must be clearly differentiated in both visual and accessible labelling.

User Experience Behaviour Supported
Users can distinguish between actions and avoid incorrect assumptions.

158. Focusable Element Validity Test

Source:

Requirement
All interactive elements must be focusable, and non-interactive elements must not be included in the focus order.

User Experience Behaviour Supported
Users can efficiently navigate only meaningful interactive elements without distraction.

159. Semantic Control Usage Test

Source: and

Requirement
Interactive controls must use appropriate semantic elements (e.g. button, link, input) rather than non-semantic substitutes.

User Experience Behaviour Supported
Users receive consistent behaviour, roles, and interaction patterns across assistive technologies.

160. Control Activation Behaviour Test

Source:

Requirement
Controls must respond correctly to standard interaction methods (keyboard, touch, pointer) using expected activation patterns.

User Experience Behaviour Supported
Users can operate controls predictably using their preferred input method.

161. Focus Order Logical Sequence Test

Source:

Requirement
Focus order must follow a logical sequence aligned with the visual and reading order of content.

User Experience Behaviour Supported
Users can navigate content in a meaningful and intuitive progression.

162. Dynamic Content Focus Placement Test

Source:

Requirement
When new content appears, it must be inserted into the focus order in a way that preserves logical navigation.

User Experience Behaviour Supported
Users can continue navigation without losing context when interfaces update dynamically.

163. Focus Style Visibility Test

Source: and

Requirement
Focused elements must have a clearly visible and distinguishable visual style.

User Experience Behaviour Supported
Users can always identify their current position within the interface.

164. Focus Indicator Contrast and Perceptibility Test

Source:

Requirement
Focus indicators must have sufficient contrast, size, and visibility to be easily perceived against surrounding content.

User Experience Behaviour Supported
Users can reliably detect focus even in complex or visually dense interfaces.

165. Focus Visibility Persistence Test

Source:

Requirement
Focus indicators must not be removed or suppressed without providing an equally visible alternative.

User Experience Behaviour Supported
Users are never left without a clear indication of focus location.

166. Hidden Focusable Element Visibility Test

Source:

Requirement
Elements that can receive focus must be visible when focused, even if hidden by default.

User Experience Behaviour Supported
Users are not confused by focus moving to unseen elements.

167. Tabindex Misuse Prevention Test

Source: and

Requirement
Positive tabindex values must not be used to override natural focus order in a way that disrupts navigation.

User Experience Behaviour Supported
Users experience predictable navigation aligned with document structure.

168. Programmatic Focus Appropriateness Test

Source:

Requirement
Programmatic focus changes must only occur where necessary and must provide appropriate context.

User Experience Behaviour Supported
Users understand why focus has moved and where they are within the interface.

169. Focus Context Communication Test

Source:

Requirement
When focus is moved programmatically, sufficient contextual information must be conveyed to the user.

User Experience Behaviour Supported
Users maintain situational awareness during interface changes.

170. Navigation Component Accessibility Test

Source:

Requirement
Global navigation components must be fully operable, structured semantically, and accessible across all input methods.

User Experience Behaviour Supported
Users can reliably navigate across products and sections regardless of device or ability.

171. Navigation Focus Management Test

Source:

Requirement
Focus must be correctly managed when navigation menus open and close, including appropriate focus placement and return.

User Experience Behaviour Supported
Users can move through navigation structures without losing orientation.

172. Hidden Navigation Content Accessibility Test

Source:

Requirement
Content hidden from view must also be removed from the accessibility tree and all input methods.

User Experience Behaviour Supported
Users are not exposed to inaccessible or irrelevant navigation options.

173. Navigation Keyboard Interaction Test

Source:

Requirement
Navigation elements must support standard keyboard interactions (e.g. Enter, Space, Escape).

User Experience Behaviour Supported
Users can operate navigation components without relying on pointer input.

174. Reduced Motion Preference Respect Test

Source:

Requirement
Animations must respect user preferences for reduced motion and be suppressed where requested.

User Experience Behaviour Supported
Users sensitive to motion are not exposed to discomfort or distraction.

175. Minimum Text Size Compliance Test

Source:

Requirement
All visible text must meet minimum size thresholds (e.g. 13px for core content, 11px for supporting content).

User Experience Behaviour Supported
Users can read content comfortably without needing to adjust browser settings.

176. Text Readability Baseline Test

Source:

Requirement
Text sizing must support readability without assuming users will apply zoom or assistive adjustments.

User Experience Behaviour Supported
Users can access content effectively in default viewing conditions.

177. Alternative Text Presence Test

Source:

Requirement
All non-decorative images and graphical elements must include alternative text that provides a text-based equivalent.

User Experience Behaviour Supported
Users who cannot see images receive equivalent access to information conveyed visually.

178. Alternative Text Relevance and Purpose Test

Source:

Requirement
Alternative text must communicate the meaning and purpose of the image within its context, not just describe its appearance.

User Experience Behaviour Supported
Users understand why the image is present and how it contributes to the content.

179. Decorative Image Exclusion Test

Source:

Requirement
Purely decorative images must have empty alternative text and be ignored by assistive technologies.

User Experience Behaviour Supported
Users are not burdened with irrelevant or redundant information.

180. Alternative Text Non-Duplication Test

Source:

Requirement
Alternative text must not duplicate information already present in surrounding text or captions.

User Experience Behaviour Supported
Users receive concise, non-repetitive information.

181. Functional Image Labelling Test

Source:

Requirement
Images used as controls must have alternative text describing the action they perform rather than their visual appearance.

User Experience Behaviour Supported
Users can understand and operate controls effectively.

182. Complex Image Summary Test

Source:

Requirement
Charts, graphs, and complex visuals must provide a summary of key trends or patterns, with access to detailed data where necessary.

User Experience Behaviour Supported
Users can understand high-level insights and access detailed information if needed.

183. Contextual Alternative Text Test

Source:

Requirement
Alternative text must adapt to the context in which the image is used, rather than being reused generically.

User Experience Behaviour Supported
Users receive accurate, context-specific information.

184. Link Text Descriptiveness Test

Source: and

Requirement
Link text must clearly describe the destination or purpose of the link independently of surrounding content.

User Experience Behaviour Supported
Users can understand and navigate links when presented in isolation (e.g. screen reader link lists).

185. Link Context Independence Test

Source:

Requirement
Links must remain understandable when read without surrounding page context.

User Experience Behaviour Supported
Users navigating via link lists or shortcuts can identify destinations accurately.

186. Repeated Link Combination Test

Source:

Requirement
Adjacent links pointing to the same destination must be combined into a single actionable element.

User Experience Behaviour Supported
Users experience reduced navigation effort and clearer interaction targets.

187. Duplicate Link Announcement Prevention Test

Source:

Requirement
Combined links must be announced once by assistive technologies, not as multiple equivalent items.

User Experience Behaviour Supported
Users avoid confusion and unnecessary repetition during navigation.

188. Unique Link Identification Test

Source:

Requirement
Links with identical visible text must include additional accessible labelling to distinguish their purpose.

User Experience Behaviour Supported
Users can differentiate between similar actions and select the correct one.

189. Visually Hidden Context Support Test

Source: and

Requirement
Additional context may be provided using visually hidden text where necessary to enhance clarity without cluttering the UI.

User Experience Behaviour Supported
Users of assistive technologies receive sufficient context while visual simplicity is preserved.

190. External Link Disclosure Test

Source:

Requirement
Links to external sites must clearly indicate that the user is leaving the current context.

User Experience Behaviour Supported
Users are aware of transitions between systems and potential changes in experience.

191. New Tab Behaviour Disclosure Test

Source:

Requirement
Links that open in new tabs or windows must communicate this behaviour to users.

User Experience Behaviour Supported
Users are not disoriented by unexpected navigation behaviour.

192. Link Accessible Name Completeness Test

Source:

Requirement
All links must have a complete accessible name derived from text or alternative text.

User Experience Behaviour Supported
Users relying on assistive technologies can identify and interact with links accurately.

193. Link Semantic Role Accuracy Test

Source:

Requirement
Links must be used strictly for navigation, and not for actions that should be implemented as buttons.

User Experience Behaviour Supported
Users experience consistent and predictable interaction patterns.

194. Link Target Size and Spacing Test

Source:

Requirement
Links must provide sufficient clickable/tappable area and spacing to support accurate interaction.

User Experience Behaviour Supported
Users with motor impairments or on small devices can interact without error.

195. Link Focus Visibility Test

Source:

Requirement
Links must provide a clear, visible focus indicator when navigated via keyboard.

User Experience Behaviour Supported
Users can track navigation position reliably.

196. Link Alternative Content Provision Test

Source:

Requirement
Links to alternative formats (e.g. PDF, external apps) must clearly indicate the format and behaviour.

User Experience Behaviour Supported
Users can anticipate and prepare for changes in format or application context.

197. Alternative Format Warning Test

Source:

Requirement
Users must be warned before content opens in a different format or external application.

User Experience Behaviour Supported
Users avoid confusion and maintain orientation.

198. Search Landmark Identification Test

Source:

Requirement
Search functionality must be exposed as a dedicated landmark to support navigation by assistive technologies.

User Experience Behaviour Supported
Users can quickly locate and access search functionality.

199. Search Input Labelling Test

Source:

Requirement
Search inputs must have properly associated labels, even if visually hidden.

User Experience Behaviour Supported
Users understand the purpose of the input field.

200. Search Suggestion Announcement Test

Source:

Requirement
Dynamic search suggestions must be communicated to assistive technologies without disrupting focus.

User Experience Behaviour Supported
Users are informed of available suggestions without losing their place.

201. Share Tools Discoverability Test

Source:

Requirement
Share tools must be structured within identifiable landmarks and labelled appropriately.

User Experience Behaviour Supported
Users can locate sharing functionality when needed.

202. Share Tools Skip Mechanism Test

Source:

Requirement
A mechanism must exist to bypass share tool controls using keyboard navigation.

User Experience Behaviour Supported
Users can avoid unnecessary navigation effort.

203. Share Tool Accessible Labelling Test

Source:

Requirement
Each share action must include clear, descriptive accessible labels, including context such as platform and behaviour.

User Experience Behaviour Supported
Users understand the purpose and outcome of each share option.

204. Site Menu Structural Semantics Test

Source:

Requirement
Site menus must use nested list structures to represent hierarchical navigation.

User Experience Behaviour Supported
Users understand relationships between navigation items.

205. Site Menu Expand/Collapse State Test

Source:

Requirement
Expandable menu items must expose their state (expanded/collapsed) programmatically.

User Experience Behaviour Supported
Users understand current navigation state and available options.

206. Site Menu Current Item Identification Test

Source:

Requirement
The current page must be indicated within navigation using appropriate semantics.

User Experience Behaviour Supported
Users can orient themselves within the site structure.

207. Visual vs Source Order Alignment Test

Source:

Requirement
The logical reading order in the source must align with the intended meaning of content, regardless of visual layout.

User Experience Behaviour Supported
Users of assistive technologies receive content in a coherent sequence.

208. Layout Reordering Safety Test

Source:

Requirement
CSS-based visual reordering must not disrupt the semantic or reading order of content.

User Experience Behaviour Supported
Users are not misled by discrepancies between visual and logical structure.

209. Tab Order Alignment with Layout Test

Source:

Requirement
Keyboard navigation order must follow the logical reading direction and layout expectations.

User Experience Behaviour Supported
Users can navigate predictably using the keyboard.

210. Audio Control Separation Test

Source:

Requirement
Audio components must provide separate volume controls for different sound types (e.g. speech, music, effects).

User Experience Behaviour Supported
Users can tailor audio output to their sensory and cognitive needs.

211. Audio Muting Independence Test

Source:

Requirement
Users must be able to mute audio independently of system-level controls.

User Experience Behaviour Supported
Users maintain control over auditory experiences.

212. Audio Accessibility for Assistive Technology Test

Source:

Requirement
Audio must not interfere with assistive technologies such as screen readers.

User Experience Behaviour Supported
Users can simultaneously access system feedback and media content.

213. Container Structural Semantics Test

Source:

Requirement
Pages must use structural containers or sectioning elements to define major regions of content.

User Experience Behaviour Supported
Users can perceive and understand how content is grouped and organised across the page.

214. Landmark Navigation Availability Test

Source:

Requirement
All major page regions must be exposed as navigable landmarks for assistive technologies.

User Experience Behaviour Supported
Users can quickly move between key sections without traversing all intermediate content.

215. Complete Content Containment Test

Source:

Requirement
All content must be contained within defined structural containers or landmark regions.

User Experience Behaviour Supported
Users experience a fully structured and navigable interface without “orphaned” content.

216. Appropriate Landmark Role Usage Test

Source: and

Requirement
Landmark roles must correctly reflect the purpose of the content they contain (e.g. navigation, main, complementary).

User Experience Behaviour Supported
Users can accurately interpret the role and purpose of each region.

217. Single Main Landmark Test

Source:

Requirement
Each page must contain exactly one main landmark representing the primary content.

User Experience Behaviour Supported
Users can reliably locate the core content of the page.

218. Landmark-Based Navigation Efficiency Test

Source:

Requirement
Landmarks must enable users to bypass repeated or peripheral content such as navigation and headers.

User Experience Behaviour Supported
Users can efficiently reach desired content without unnecessary navigation effort.

219. Skip Link Availability Test

Source:

Requirement
A skip mechanism must be provided to allow users to jump directly to main content.

User Experience Behaviour Supported
Keyboard users can avoid repetitive navigation through global elements.

220. Skip Link Placement and Visibility Test

Source:

Requirement
Skip links must be placed at the beginning of the page and become visible when focused.

User Experience Behaviour Supported
Users can discover and use skip functionality when navigating via keyboard.

221. Heading Presence Test

Source:

Requirement
All significant content sections must include appropriate headings where supported by the platform.

User Experience Behaviour Supported
Users can scan and navigate content efficiently.

222. Heading Hierarchical Structure Test

Source: and

Requirement
Headings must follow a logical hierarchical order without skipping levels.

User Experience Behaviour Supported
Users can understand relationships between sections and sub-sections.

223. Single Primary Heading Test

Source:

Requirement
Each page must include a single primary heading representing the main topic.

User Experience Behaviour Supported
Users can immediately identify the purpose of the page.

224. Heading Content Association Test

Source:

Requirement
Each heading must be followed by content that it clearly describes.

User Experience Behaviour Supported
Users can interpret headings as meaningful labels for content sections.

225. Heading Semantic Integrity Test

Source:

Requirement
Only true headings must use heading elements; visual styling alone must not be used to simulate headings.

User Experience Behaviour Supported
Users relying on assistive technologies can accurately identify navigable sections.

226. Heading Descriptiveness Test

Source:

Requirement
Headings must clearly and concisely describe the content they introduce.

User Experience Behaviour Supported
Users can quickly locate relevant sections without reading full content.

227. Heading Navigability Test

Source:

Requirement
Headings must be programmatically identifiable to support navigation via assistive technologies.

User Experience Behaviour Supported
Users can jump between sections efficiently using heading navigation tools.

228. Heading Visual Distinction Test

Source:

Requirement
Headings must be visually distinguishable from surrounding content.

User Experience Behaviour Supported
Users can visually scan and identify structure quickly.

229. Landmark Label Clarity Test

Source:

Requirement
Landmarks must have clear, descriptive labels where necessary to distinguish between similar regions.

User Experience Behaviour Supported
Users can differentiate between multiple navigation or complementary regions.

230. Landmark Semantic Element Preference Test

Source:

Requirement
Native HTML sectioning elements must be used in preference to non-semantic containers where possible.

User Experience Behaviour Supported
Users benefit from consistent and reliable structural semantics.

231. Role Assignment Accuracy Test

Source:

Requirement
All elements must have correct roles assigned, either natively or via accessibility properties.

User Experience Behaviour Supported
Users understand how each element behaves and how to interact with it.

232. Accessible Name Provision Test

Source:

Requirement
All interactive and relevant elements must have an accessible name.

User Experience Behaviour Supported
Users can identify elements and their purpose through assistive technologies.

233. State Communication Test

Source:

Requirement
Element states (e.g. expanded, selected, checked) must be programmatically conveyed and updated.

User Experience Behaviour Supported
Users understand current status and changes in interface elements.

234. Value Communication Test

Source:

Requirement
Where applicable, element values must be exposed to assistive technologies.

User Experience Behaviour Supported
Users can perceive current values (e.g. input fields, sliders).

235. State Change Announcement Test

Source:

Requirement
Changes in element state must be announced to assistive technologies when they occur.

User Experience Behaviour Supported
Users are informed of dynamic changes in real time.

236. Native Control Preference Test

Source:

Requirement
Native platform controls must be used where possible instead of custom-built components.

User Experience Behaviour Supported
Users benefit from consistent, well-supported interaction patterns.

237. Custom Control Accessibility Completion Test

Source:

Requirement
Custom components must fully implement roles, names, states, and behaviours equivalent to native controls.

User Experience Behaviour Supported
Users can interact with custom elements as reliably as standard ones.

238. Form Submission Trigger Control Test

Source:

Requirement
Form submission or navigation changes must only occur on explicit user action (e.g. activating a submit button), not on focus, blur, or input change events.

User Experience Behaviour Supported
Users remain in control of the interaction flow and are not disrupted by unexpected changes while completing a form.

239. Form Submit Mechanism Presence Test

Source:

Requirement
All forms that collect user input must include a clearly identifiable submit mechanism.

User Experience Behaviour Supported
Users can understand how to complete and submit a form without ambiguity.

240. Form Keyboard Completion Test

Source:

Requirement
Forms must be fully operable, including completion, correction, and submission, using only a keyboard.

User Experience Behaviour Supported
Users who cannot use a mouse or touch input can independently complete tasks.

241. Form Tab Order Predictability Test

Source:

Requirement
The tabbing sequence through form fields must be logical and consistent with the visual layout.

User Experience Behaviour Supported
Users can move through the form in a predictable and efficient order.

242. Required Field Identification Test

Source: and

Requirement
Required fields must be clearly indicated both visually and programmatically.

User Experience Behaviour Supported
Users understand which fields must be completed before submission.

243. Error Message Specificity Test

Source:

Requirement
Error messages must clearly identify which field is invalid, why it is invalid, and how to correct it.

User Experience Behaviour Supported
Users can quickly understand and resolve errors without confusion.

244. Error Message Tone and Clarity Test

Source:

Requirement
Error messages must be concise, clear, and supportive in tone.

User Experience Behaviour Supported
Users feel guided rather than blamed, reducing frustration and abandonment.

245. Error Message Visibility and Placement Test

Source:

Requirement
Error messages must be displayed near the relevant form control and be clearly visible.

User Experience Behaviour Supported
Users can easily associate errors with the correct fields.

246. Error Message Programmatic Association Test

Source:

Requirement
Error messages must be programmatically associated with their corresponding form fields.

User Experience Behaviour Supported
Assistive technology users can understand which inputs require correction.

247. Error State Announcement Test

Source:

Requirement
Error states must be communicated to assistive technologies when they occur.

User Experience Behaviour Supported
Users receive immediate feedback about validation issues.

248. Input Preservation on Error Test

Source:

Requirement
User-entered data must not be cleared when validation errors occur.

User Experience Behaviour Supported
Users can correct mistakes without re-entering information.

249. Inline Validation Timing Test

Source:

Requirement
Validation feedback must not interrupt users during input; it should occur at appropriate interaction points (e.g. on submission).

User Experience Behaviour Supported
Users can complete input without distraction or cognitive overload.

250. General Error Summary Test

Source:

Requirement
A general error summary must be provided when multiple validation errors occur.

User Experience Behaviour Supported
Users can quickly understand that multiple issues exist and locate them efficiently.

251. Error Identification Without Colour Test

Source:

Requirement
Error states must not rely solely on colour to convey meaning.

User Experience Behaviour Supported
Users with colour perception limitations can still identify errors.

252. Placeholder Non-Substitution Test

Source: and

Requirement
Placeholder text must not be used as a substitute for visible labels.

User Experience Behaviour Supported
Users retain persistent context about what each field requires.

253. Label and Accessible Name Consistency Test

Source: and

Requirement
The accessible name of a control must match or closely align with its visible label.

User Experience Behaviour Supported
Users of assistive technologies and voice input systems experience consistent interaction.

254. Label Persistence Test

Source:

Requirement
Labels must remain visible and not disappear when users begin interacting with inputs.

User Experience Behaviour Supported
Users maintain context throughout the interaction.

255. Form Field Instruction Association Test

Source:

Requirement
Instructions or hints must be programmatically associated with their corresponding form fields.

User Experience Behaviour Supported
Users receive necessary guidance at the point of interaction.

256. Input Type Appropriateness Test

Source:

Requirement
Appropriate input types must be used to match expected data (e.g. numeric, date, email).

User Experience Behaviour Supported
Users can input data efficiently with reduced errors.

257. Autocomplete Support Test

Source:

Requirement
Form fields collecting known data types must support autocomplete where appropriate.

User Experience Behaviour Supported
Users can complete forms more quickly with reduced effort.

258. Form Group Labelling Test

Source: and

Requirement
Groups of related form controls must have a shared label using appropriate grouping mechanisms.

User Experience Behaviour Supported
Users understand relationships between grouped inputs.

259. Radio and Checkbox Group Association Test

Source:

Requirement
Radio buttons and checkboxes must be grouped correctly to reflect a single logical input.

User Experience Behaviour Supported
Users understand available options and selection constraints.

260. Group Context Communication Test

Source:

Requirement
Grouped controls must provide contextual information that distinguishes similar inputs.

User Experience Behaviour Supported
Users can differentiate between similar groups (e.g. billing vs delivery address).

261. Form Layout Logical Association Test

Source:

Requirement
Form layout must visually and structurally associate labels with their controls.

User Experience Behaviour Supported
Users can easily identify which label corresponds to which field.

262. Label Proximity Test

Source:

Requirement
Labels must be positioned in close proximity to their associated inputs.

User Experience Behaviour Supported
Users, particularly those using magnification, can maintain context.

263. Label Positioning Consistency Test

Source:

Requirement
Labels must be positioned consistently relative to inputs (e.g. above or left).

User Experience Behaviour Supported
Users can predict and interpret form structure quickly.

264. Label Click Focus Behaviour Test

Source:

Requirement
Activating a label must move focus to the associated form control.

User Experience Behaviour Supported
Users can interact more easily, especially on touch devices.

265. Accessible Name Completeness for Inputs Test

Source:

Requirement
All form inputs must expose a complete and meaningful accessible name.

User Experience Behaviour Supported
Users of assistive technologies can identify each field’s purpose.

266. Instruction Placement Order Test

Source:

Requirement
Instructions must appear after labels and before input fields.

User Experience Behaviour Supported
Users receive guidance at the correct point in the interaction flow.

267. Error Message Persistence Test

Source:

Requirement
Error messages must persist until the user resolves the issue.

User Experience Behaviour Supported
Users have sufficient time to read and act on feedback.

268. Error Message Presence and Perceivability Test

Source:

Requirement
All error states must be communicated through messages that are both visible and perceivable by assistive technologies.

User Experience Behaviour Supported
Users can detect when an error has occurred regardless of sensory modality.

269. Error Correction Guidance Test

Source:

Requirement
Error messages must include clear instructions or suggestions explaining how to correct the error.

User Experience Behaviour Supported
Users can recover from errors independently without external assistance.

270. Error Location Identification Test

Source:

Requirement
Error messages must clearly identify the specific fields or controls requiring correction.

User Experience Behaviour Supported
Users can efficiently locate and address issues within complex forms.

271. Error Navigation and Focus Return Test

Source:

Requirement
Users must be able to easily navigate to and return focus to fields containing errors.

User Experience Behaviour Supported
Users can correct errors without disorientation or excessive navigation effort.

272. Error Summary Announcement Test

Source:

Requirement
When multiple errors occur, a summary must be presented and announced (e.g. via live region) to assistive technologies.

User Experience Behaviour Supported
Users receive an overview of issues and can plan corrective actions.

273. Error Notification Without Keyboard Trap Test

Source:

Requirement
Error handling mechanisms must not introduce keyboard traps or prevent normal navigation.

User Experience Behaviour Supported
Keyboard users retain full control of interaction flow.

274. Error Alert Modal Behaviour Test

Source:

Requirement
If error messages are presented in dialogs or alerts, they must be accessible, announced, and allow return to the relevant context.

User Experience Behaviour Supported
Users understand and can act on critical interruptions without losing context.

275. Assistance Availability Test

Source:

Requirement
Optional help, hints, or assistance must be available where users may struggle to complete tasks.

User Experience Behaviour Supported
Users receive support when needed, reducing abandonment.

276. Context-Sensitive Help Test

Source:

Requirement
Help and guidance must be relevant to the current task or input context.

User Experience Behaviour Supported
Users receive targeted assistance that improves task completion.

277. Assistance Discoverability Test

Source:

Requirement
Help content must be easy to locate within the interface.

User Experience Behaviour Supported
Users can access support without unnecessary effort.

278. Assistance Modality Test

Source:

Requirement
Assistance must be available both visually and through assistive technologies.

User Experience Behaviour Supported
All users can perceive and benefit from guidance.

279. Feedback Appropriateness Test

Source:

Requirement
Feedback must be helpful and not overwhelming or intrusive.

User Experience Behaviour Supported
Users remain focused and are not cognitively overloaded.

280. Action Dialog Role and Semantics Test

Source:

Requirement
Dialogs requiring user action must use appropriate semantic roles and accessible naming.

User Experience Behaviour Supported
Assistive technologies correctly interpret dialog purpose and content.

281. Action Dialog Focus Management Test

Source:

Requirement
Focus must move into the dialog when opened and return to the invoking element when closed.

User Experience Behaviour Supported
Users maintain orientation and control during modal interactions.

282. Action Dialog Modal Isolation Test

Source:

Requirement
Background content must become non-interactive while a modal dialog is active.

User Experience Behaviour Supported
Users are not distracted or confused by inactive elements.

283. Action Dialog Invocation Control Test

Source:

Requirement
Dialogs must not appear unexpectedly without user action except in justified cases.

User Experience Behaviour Supported
Users are not disrupted by unexpected interruptions.

284. Action Dialog Control Accessibility Test

Source:

Requirement
All dialog controls must be accessible, focusable, and clearly labelled.

User Experience Behaviour Supported
Users can interact with dialog options effectively.

285. Button vs Link Semantic Accuracy Test

Source:

Requirement
Interactive elements must use correct semantics (buttons for actions, links for navigation).

User Experience Behaviour Supported
Users can predict behaviour and interact confidently.

286. Button and CTA Label Clarity Test

Source:

Requirement
Buttons and CTAs must have clear, descriptive text labels.

User Experience Behaviour Supported
Users understand the outcome of activating controls.

287. Icon-Only Control Accessibility Test

Source:

Requirement
Icon-only controls must include accessible text alternatives.

User Experience Behaviour Supported
Users relying on assistive technologies can understand control purpose.

288. Button State Communication Test

Source:

Requirement
Changes in button state must be clearly indicated visually and programmatically.

User Experience Behaviour Supported
Users understand system status and interaction outcomes.

289. Disabled Control Usability Test

Source:

Requirement
Disabled controls must remain perceivable and not create confusion in navigation.

User Experience Behaviour Supported
Users understand available actions without losing context.

290. Grouped Component Representation Test

Source:

Requirement
Compound UI elements must be represented as a single logical control.

User Experience Behaviour Supported
Users experience simplified and efficient interaction.

291. Grouping Semantic Structure Test

Source:

Requirement
Grouped elements must use appropriate semantic structures or ARIA roles.

User Experience Behaviour Supported
Assistive technologies convey relationships between elements accurately.

292. Grouped Element Announcement Test

Source:

Requirement
Grouped controls must be announced as a unified component rather than separate elements.

User Experience Behaviour Supported
Users understand complex controls without cognitive overload.

293. Notification Multi-Modal Delivery Test

Source:

Requirement
Notifications must be delivered through multiple modalities (visual, auditory, and where appropriate tactile).

User Experience Behaviour Supported
Users perceive notifications regardless of sensory ability.

294. Notification State Change Announcement Test

Source:

Requirement
Changes in content state must be communicated to assistive technologies.

User Experience Behaviour Supported
Users are aware of dynamic updates.

295. Notification Non-Disruptive Behaviour Test

Source: and

Requirement
Non-critical notifications must not steal focus or interrupt user tasks.

User Experience Behaviour Supported
Users can continue their task without disruption.

296. Standard Notification Usage Test

Source:

Requirement
Where possible, standard operating system notifications must be used.

User Experience Behaviour Supported
Users benefit from familiar, accessible notification patterns.

297. Tabindex Logical Order Test

Source:

Requirement
Focus order must follow the natural document structure without using positive tabindex values.

User Experience Behaviour Supported
Users navigate content in a predictable order.

298. Tabindex Misuse Prevention Test

Source:

Requirement
Tabindex must not be used to artificially create interactivity on non-interactive elements.

User Experience Behaviour Supported
Users interact only with meaningful controls.

299. Programmatic Focus Management Test

Source:

Requirement
Programmatic focus changes must use appropriate tabindex values and patterns.

User Experience Behaviour Supported
Users are guided to relevant content without confusion.

300. Timeout Adjustability Test

Source:

Requirement
Users must be able to extend, adjust, or disable time limits.

User Experience Behaviour Supported
Users can complete tasks at their own pace.

301. Timeout Warning Test

Source:

Requirement
Users must be warned in advance before a timeout occurs.

User Experience Behaviour Supported
Users have time to act before losing progress.

302. Timeout Data Loss Prevention Test

Source:

Requirement
Users must be informed if data will be lost due to timeout.

User Experience Behaviour Supported
Users can make informed decisions about continuing or saving work.

303. Title Attribute Misuse Test

Source:

Requirement
Title attributes must not be used to convey essential information.

User Experience Behaviour Supported
Users are not dependent on inaccessible or undiscoverable content.

304. Title Attribute Redundancy Test

Source:

Requirement
Title attributes must not duplicate visible content unnecessarily.

User Experience Behaviour Supported
Users avoid redundant or confusing information.

305. Title Attribute Accessibility Limitation Test

Source:

Requirement
Title attributes must not be relied upon for labels or instructions due to inconsistent accessibility support.

User Experience Behaviour Supported
Users receive critical information through reliable channels.

306. Breadcrumb Navigation Presence Test

Source:

Requirement
Breadcrumb navigation must be provided for hierarchical content structures where appropriate.

User Experience Behaviour Supported
Users can understand their location within a structure and navigate backwards efficiently.

307. Breadcrumb Structural Semantics Test

Source:

Requirement
Breadcrumbs must be implemented as a list within a navigation landmark with an appropriate accessible name.

User Experience Behaviour Supported
Assistive technology users can identify and navigate breadcrumb structures effectively.

308. Breadcrumb Current Page Identification Test

Source:

Requirement
The current page within breadcrumbs must be clearly indicated and not presented as a link.

User Experience Behaviour Supported
Users can distinguish between navigable items and the current location.

309. Breadcrumb Separator Non-Announcement Test

Source:

Requirement
Visual separators between breadcrumb items must not be announced by assistive technologies.

User Experience Behaviour Supported
Users are not exposed to unnecessary or confusing auditory clutter.

310. Comments Landmark Identification Test

Source:

Requirement
Comments sections must be identified as a complementary landmark with a clear accessible label.

User Experience Behaviour Supported
Users can locate and navigate to comments independently of main content.

311. Comments Section Heading Clarity Test

Source:

Requirement
The comments section must include a descriptive heading that conveys purpose and encourages participation.

User Experience Behaviour Supported
Users understand the purpose of the section and how to engage with it.

312. Comment Form Accessibility Test

Source:

Requirement
Comment input fields must be properly labelled, described, and include associated validation and feedback.

User Experience Behaviour Supported
Users can contribute content confidently and correctly.

313. Comment Character Count Communication Test

Source:

Requirement
Character limits must be communicated dynamically and accessibly.

User Experience Behaviour Supported
Users can manage input constraints without error or confusion.

314. Comment Submission Feedback Test

Source:

Requirement
Successful comment submission must be communicated via a live region or equivalent mechanism.

User Experience Behaviour Supported
Users receive confirmation that their action was completed.

315. Comment Stream Structural List Test

Source:

Requirement
Comments must be structured as a list, with replies nested appropriately.

User Experience Behaviour Supported
Users can understand relationships between comments and replies.

316. Comment Heading Uniqueness Test

Source:

Requirement
Each comment heading must include sufficient information (e.g. author and timestamp) to be unique.

User Experience Behaviour Supported
Users can differentiate between comments when navigating by headings.

317. Comment Interaction Control Accessibility Test

Source:

Requirement
All comment interaction controls (reply, like, share, etc.) must be accessible and clearly labelled.

User Experience Behaviour Supported
Users can fully participate in interaction features.

318. External Link Context Change Warning Test

Source:

Requirement
External links must indicate that they lead to a different domain or context.

User Experience Behaviour Supported
Users are prepared for navigation to unfamiliar environments.

319. External Link Icon Usage Test

Source:

Requirement
External links must include a visual indicator such as an icon.

User Experience Behaviour Supported
Sighted users can quickly identify external destinations.

320. External Link Screen Reader Warning Test

Source:

Requirement
External links must include non-visible text indicating the context change.

User Experience Behaviour Supported
Screen reader users are informed before navigating away.

321. External Link List Structure Test

Source:

Requirement
Collections of external links must be grouped using list structures and introduced with a heading.

User Experience Behaviour Supported
Users can scan and navigate lists of related resources efficiently.

322. Filter Navigation Landmark Test

Source:

Requirement
Filtering controls must be contained within a navigation landmark with a clear label.

User Experience Behaviour Supported
Users can locate filtering tools quickly.

323. Filter Option Structure Test

Source:

Requirement
Filter options must be implemented as lists of links representing discrete states.

User Experience Behaviour Supported
Users can understand and select filtering criteria predictably.

324. Filter Current State Indication Test

Source:

Requirement
The currently applied filter and sort options must be clearly indicated.

User Experience Behaviour Supported
Users understand the current context of displayed results.

325. Filter Progressive Enhancement Test

Source:

Requirement
Filtering functionality must work without reliance on JavaScript, with enhancements layered on top.

User Experience Behaviour Supported
Users can access core functionality regardless of technical constraints.

326. Load More User Control Test

Source:

Requirement
Content loading must be triggered explicitly by user action (e.g. a “Load more” button).

User Experience Behaviour Supported
Users control content flow and are not overwhelmed by automatic loading.

327. Load More Feedback and Announcement Test

Source:

Requirement
Loading states must be communicated visually and via assistive technologies.

User Experience Behaviour Supported
Users understand when content is being loaded.

328. Load More Content Insertion Awareness Test

Source:

Requirement
Newly loaded content must be clearly introduced and identifiable within the content stream.

User Experience Behaviour Supported
Users can perceive where new content begins.

329. Load More Focus Management Test

Source:

Requirement
Focus must be managed so users can continue interacting with newly loaded content.

User Experience Behaviour Supported
Users do not lose their place during dynamic updates.

330. Metadata Strip Semantic Clarity Test

Source:

Requirement
Metadata must be structured as a list with clear semantic meaning.

User Experience Behaviour Supported
Users can interpret contextual information about content.

331. Metadata Non-Visual Equivalence Test

Source:

Requirement
Non-visible text must provide equivalent meaning where visual representations are insufficient.

User Experience Behaviour Supported
Users relying on assistive technologies receive complete information.

332. Metadata Link Distinguishability Test

Source:

Requirement
Links within metadata must not rely on colour alone for identification.

User Experience Behaviour Supported
Users can identify links regardless of visual limitations.

333. Page Title Presence Test

Source:

Requirement
Every page must include a descriptive title element.

User Experience Behaviour Supported
Users can identify and orient themselves within content.

334. Page Title Descriptiveness Test

Source:

Requirement
Page titles must clearly describe the primary content and context.

User Experience Behaviour Supported
Users understand where they are within the site or application.

335. SPA Title Update Test

Source:

Requirement
In dynamic applications, page titles must update when content changes.

User Experience Behaviour Supported
Users receive accurate contextual information during navigation.

336. SPA Focus Reset Test

Source:

Requirement
Focus must move to the top of new content when views change dynamically.

User Experience Behaviour Supported
Users can begin navigating new content predictably.

337. SPA Navigation History Integrity Test

Source:

Requirement
Application routing must preserve expected browser navigation behaviour (back/forward).

User Experience Behaviour Supported
Users can navigate using familiar browser controls.

338. Tooltip Non-Duplication Test

Source:

Requirement
Tooltips must not duplicate information already available in labels or content.

User Experience Behaviour Supported
Users avoid redundant or repetitive information.

339. Tooltip Non-Essential Information Test

Source:

Requirement
Tooltips must not contain essential information required to complete tasks.

User Experience Behaviour Supported
Users are not dependent on inaccessible or hidden content.

340. Tooltip Supplementary Value Test

Source:

Requirement
Tooltips must provide additional, contextual information rather than core content.

User Experience Behaviour Supported
Users receive helpful enhancements without reliance.

341. Unique Page Title Requirement Test

Source:

Requirement
Each page or screen must have a unique, context-sensitive title.

User Experience Behaviour Supported
Users can distinguish between different pages and maintain orientation.

342. Visible Screen Title Test

Source:

Requirement
Each screen must include a visible title or equivalent identifier.

User Experience Behaviour Supported
Users can visually confirm their location within the interface.

343. Screen Title Announcement Test

Source:

Requirement
Page or screen titles must be announced by assistive technologies when content loads.

User Experience Behaviour Supported
Users receive immediate orientation cues.

344. Accordion Region Identification Test

Source:

Requirement
Accordion components must be contained within a region element with an accessible name that describes the grouped content.

User Experience Behaviour Supported
Users can identify the accordion as a related collection of content sections.

345. Accordion Control as Button Test

Source:

Requirement
Each accordion section must be controlled by a button element within a heading.

User Experience Behaviour Supported
Users can interact with accordion controls using standard keyboard and assistive technology conventions.

346. Accordion aria-controls Association Test

Source:

Requirement
Accordion control buttons must include an aria-controls attribute referencing the associated content panel.

User Experience Behaviour Supported
Users can understand the relationship between control and content.

347. Accordion aria-expanded State Test

Source:

Requirement
Accordion controls must expose state via aria-expanded to indicate whether content is open or closed.

User Experience Behaviour Supported
Users can determine the visibility state of content.

348. Accordion Content Visibility Management Test

Source:

Requirement
Accordion content must be hidden both visually and in the accessibility tree when collapsed.

User Experience Behaviour Supported
Users are not exposed to inaccessible or irrelevant hidden content.

349. Accordion Single-Expand Behaviour Test

Source:

Requirement
Where accordion behaviour enforces a single open section, opening one section must close others and update control states accordingly.

User Experience Behaviour Supported
Users experience predictable and manageable content expansion.

350. Accordion Native Element Support Test

Source:

Requirement
Where appropriate, native <details> and <summary> elements should be used to provide inherent accessibility without JavaScript.

User Experience Behaviour Supported
Users benefit from built-in browser accessibility behaviours.

351. Accordion Heading Structure Preservation Test

Source:

Requirement
Accordion implementations must preserve heading semantics and must not override them with inappropriate ARIA roles.

User Experience Behaviour Supported
Users navigating by headings can understand document structure.

352. Accordion Progressive Enhancement Test

Source:

Requirement
Accordion content must be available in an expanded, accessible form when JavaScript is not available.

User Experience Behaviour Supported
Users can access content regardless of technical constraints.

353. Accordion Toggle Proximity Test

Source:

Requirement
Accordion controls must immediately precede their associated content panels in the DOM.

User Experience Behaviour Supported
Users can intuitively move from control to revealed content.

354. Dialog Modal Isolation Test

Source:

Requirement
Modal dialogs must prevent interaction with background content while open.

User Experience Behaviour Supported
Users can focus on the dialog without interference.

355. Dialog Focus Initialisation Test

Source:

Requirement
Focus must move to an appropriate element within the dialog when it opens.

User Experience Behaviour Supported
Users can begin interacting with dialog content immediately.

356. Dialog Focus Return Test

Source:

Requirement
When a dialog is closed, focus must return to the element that triggered it.

User Experience Behaviour Supported
Users retain context and control flow continuity.

357. Dialog Close Mechanism Test

Source:

Requirement
Dialogs must provide a clear and accessible mechanism to close them.

User Experience Behaviour Supported
Users can exit modal contexts easily.

358. Dialog Heading Structure Test

Source:

Requirement
Dialogs must begin with a level-one heading describing their content.

User Experience Behaviour Supported
Users can understand the purpose of the dialog immediately.

359. Dialog Keyboard Activation Test

Source:

Requirement
Dialog trigger controls must be operable via keyboard (e.g. Enter, Space).

User Experience Behaviour Supported
Users can access dialogs without a mouse.

360. Reveal Control Identification Test

Source:

Requirement
Disclosure/reveal controls must be clearly presented as buttons with descriptive labels.

User Experience Behaviour Supported
Users understand the purpose of the control.

361. Reveal aria-expanded State Test

Source:

Requirement
Reveal controls must expose open/closed state via aria-expanded.

User Experience Behaviour Supported
Users can determine whether content is visible.

362. Reveal Content Association Test

Source:

Requirement
Reveal controls must reference associated content via aria-controls.

User Experience Behaviour Supported
Users can understand relationships between controls and content.

363. Reveal Content Visibility Management Test

Source:

Requirement
Hidden content must be removed from both visual display and accessibility tree when collapsed.

User Experience Behaviour Supported
Users are not exposed to irrelevant content.

364. Reveal Native Element Usage Test

Source:

Requirement
Where possible, <details> and <summary> elements should be used to implement disclosure functionality.

User Experience Behaviour Supported
Users benefit from native interaction and accessibility support.

365. Card List Structure Test

Source:

Requirement
Sets of cards must be structured as lists, with each card as a list item.

User Experience Behaviour Supported
Users can navigate card collections effectively.

366. Card Heading Hierarchy Test

Source:

Requirement
Each card must include a heading of consistent level, introduced by a higher-level section heading.

User Experience Behaviour Supported
Users can understand relationships between cards and surrounding content.

367. Card Focus Order Integrity Test

Source:

Requirement
Card heading elements must appear first in the source order to maintain logical focus order.

User Experience Behaviour Supported
Users experience predictable navigation.

368. Card Expandable Content State Test

Source:

Requirement
Expandable card sections must use aria-expanded to communicate state.

User Experience Behaviour Supported
Users understand when additional content is revealed.

369. Card Action Control Labelling Test

Source:

Requirement
Card action buttons must include accessible labels, including visually hidden text where necessary.

User Experience Behaviour Supported
Users can understand the purpose of each control.

370. Card Toggle Control State Test

Source:

Requirement
Toggle-style controls (e.g. “Love”) must use aria-pressed to indicate state.

User Experience Behaviour Supported
Users can determine current selection or activation state.

371. Information Panel Invocation State Test

Source:

Requirement
Information panel trigger buttons must expose aria-expanded and aria-haspopup states.

User Experience Behaviour Supported
Users understand that the control reveals additional content.

372. Information Panel Focus Management Test

Source:

Requirement
Focus must move into the panel when opened and return to the trigger when closed.

User Experience Behaviour Supported
Users maintain orientation during interaction.

373. Information Panel Close Interaction Test

Source:

Requirement
Panels must be closable via explicit controls, outside click, and Escape key.

User Experience Behaviour Supported
Users can dismiss panels using multiple expected methods.

374. Information Panel Accessible Labelling Test

Source:

Requirement
Panels must be labelled via aria-labelledby referencing a visible title.

User Experience Behaviour Supported
Users understand the context and purpose of the panel.

375. Information Panel Non-Essential Content Test

Source:

Requirement
Information panels must not contain essential content unless an alternative is provided.

User Experience Behaviour Supported
Users without JavaScript or panel access are not excluded.

376. Pocket Progressive Enhancement Test

Source:

Requirement
Pocket components must degrade gracefully, showing full content when JavaScript is unavailable.

User Experience Behaviour Supported
Users can access content regardless of technical capability.

377. Pocket Content Truncation Accessibility Test

Source:

Requirement
Truncated content must be hidden from assistive technologies using appropriate mechanisms (e.g. inert).

User Experience Behaviour Supported
Users are not exposed to inaccessible partial content.

378. Pocket Continue Cue Test

Source:

Requirement
A continuation cue must be inserted when content is expanded to maintain reading position.

User Experience Behaviour Supported
Users do not lose their place in long content.

379. Pocket Toggle Label Update Test

Source:

Requirement
Toggle controls must update labels (e.g. “Show more” / “Show less”) to reflect state.

User Experience Behaviour Supported
Users understand the current interaction state.

380. Pocket Focus Relocation Test

Source:

Requirement
Focus must move to the continuation point when content is expanded.

User Experience Behaviour Supported
Users can continue reading seamlessly.

381. Default Language Declaration Test

Source:

Requirement
The default language of the page or application must be defined programmatically.

User Experience Behaviour Supported
Assistive technologies can use correct pronunciation.

382. Language Change Identification Test

Source:

Requirement
Changes in language within content must be explicitly marked.

User Experience Behaviour Supported
Users receive accurate pronunciation and comprehension.

383. Multi-Language Content Coverage Test

Source:

Requirement
Language attributes must apply to all relevant content types (text, labels, media alternatives, etc.).

User Experience Behaviour Supported
Users experience consistent and accurate interpretation.

384. HTML Language Attribute Presence Test

Source:

Requirement
The <html> element must include a valid lang attribute representing the primary language.

User Experience Behaviour Supported
Users and assistive technologies can correctly interpret page content.

385. Inline Language Markup Test

Source:

Requirement
Inline content in different languages must use lang attributes to override defaults.

User Experience Behaviour Supported
Users receive correct pronunciation and contextual understanding.

386. Media Control Availability Test

Source:

Requirement
Any moving, blinking, scrolling, or auto-updating content must provide controls to pause, stop, or hide the behaviour.

User Experience Behaviour Supported
Users can manage motion and avoid distraction or cognitive overload.

387. Media Control Accessibility Test

Source:

Requirement
Controls for dynamic or animated content must be operable via assistive technologies.

User Experience Behaviour Supported
All users can control dynamic content regardless of interaction method.

388. Auto-Updating Content Time Limit Test

Source:

Requirement
Decorative or non-essential animations must stop automatically after a limited number of cycles if no control is provided.

User Experience Behaviour Supported
Users are not exposed to continuous, potentially harmful motion.

389. Breakout Box Landmark Identification Test

Source:

Requirement
Breakout boxes must be implemented using the <aside> element and labelled via aria-labelledby.

User Experience Behaviour Supported
Users can identify supplementary content as a distinct, navigable landmark.

390. Breakout Box Unique Labelling Test

Source:

Requirement
Each breakout box must have a unique accessible label describing its purpose.

User Experience Behaviour Supported
Users can distinguish between multiple supplementary content areas.

391. Breakout Box Structural Exclusion Test

Source:

Requirement
Breakout box headings must be removed from the main document outline using aria-hidden.

User Experience Behaviour Supported
Users navigating by headings are not misled by non-primary content.

392. Carousel User Control Test

Source:

Requirement
Carousel content must not auto-advance; navigation must be entirely user-controlled.

User Experience Behaviour Supported
Users can browse content at their own pace without unexpected changes.

393. Carousel Navigation Button Semantics Test

Source:

Requirement
Carousel navigation controls must be implemented as button elements with accessible labels.

User Experience Behaviour Supported
Users can reliably operate navigation controls.

394. Carousel List Structure Test

Source:

Requirement
Carousel items must be structured as a list to convey grouping and quantity.

User Experience Behaviour Supported
Users understand they are navigating a collection of related items.

395. Carousel Disabled State Test

Source:

Requirement
Navigation controls must reflect disabled states when movement is not possible.

User Experience Behaviour Supported
Users receive accurate feedback about available actions.

396. Carousel Reduced Motion Compliance Test

Source:

Requirement
Scrolling animations must respect user preferences for reduced motion.

User Experience Behaviour Supported
Users sensitive to motion are protected from unnecessary animation.

397. Data Table Semantic Structure Test

Source:

Requirement
Data tables must use proper <table>, <th>, <td>, <thead>, and <tbody> elements.

User Experience Behaviour Supported
Users can interpret tabular relationships correctly.

398. Data Table Header Presence Test

Source:

Requirement
All data tables must include column and/or row headers using <th> elements.

User Experience Behaviour Supported
Users receive contextual information when navigating cells.

399. Data Table Scope Attribute Test

Source:

Requirement
Header cells must define scope (row or column) where applicable.

User Experience Behaviour Supported
Users can correctly associate data with headers.

400. Data Table Caption Association Test

Source:

Requirement
Tables must include a <caption> element to provide an accessible label.

User Experience Behaviour Supported
Users can identify the purpose of the table immediately.

401. Data Table Scroll Container Accessibility Test

Source:

Requirement
Scrollable table containers must be keyboard accessible and labelled.

User Experience Behaviour Supported
Users can navigate large tables effectively.

402. Table Data vs Layout Identification Test

Source:

Requirement
Tables must be structured in a way that allows assistive technologies to distinguish data tables from layout tables.

User Experience Behaviour Supported
Users receive appropriate navigation and interpretation of table content.

403. Table Structural Feature Detection Test

Source:

Requirement
Tables must include structural indicators such as captions, headers, or grouping elements to be recognised as data tables.

User Experience Behaviour Supported
Users benefit from enhanced navigation and comprehension.

404. Grid Semantic Appropriateness Test

Source:

Requirement
Grid layouts must not misuse table semantics when content is not tabular.

User Experience Behaviour Supported
Users are not misled by incorrect structural cues.

405. Grid Thematic Grouping Test

Source:

Requirement
When grid items represent a related set, they must be marked up as a list.

User Experience Behaviour Supported
Users understand relationships between items.

406. Grid Landmark Usage Test

Source:

Requirement
Grid items with distinct semantic roles must use appropriate landmark elements (e.g. <main>, <aside>).

User Experience Behaviour Supported
Users can navigate page regions effectively.

407. Grid Heading Consistency Test

Source:

Requirement
Headings within grid items must follow a consistent hierarchical level.

User Experience Behaviour Supported
Users can understand structure across repeated items.

408. Promo Landmark Labelling Test

Source:

Requirement
Promo groups must be placed within a labelled <aside> or equivalent landmark.

User Experience Behaviour Supported
Users can identify related or supplementary content.

409. Promo List Structure Test

Source:

Requirement
Groups of promos must be structured as lists.

User Experience Behaviour Supported
Users understand the number and grouping of promotional items.

410. Promo Primary Link Test

Source:

Requirement
Each promo must have a single primary link acting as its headline.

User Experience Behaviour Supported
Users can clearly identify the navigation target.

411. Promo Image Accessibility Test

Source:

Requirement
Promo images must include appropriate alternative text or be marked as decorative.

User Experience Behaviour Supported
Users receive meaningful or non-redundant descriptions.

412. Promo Redundant Link Avoidance Test

Source:

Requirement
Images within promos must not create additional redundant links.

User Experience Behaviour Supported
Users are not forced through unnecessary navigation steps.

413. Tabs Progressive Enhancement Test

Source:

Requirement
Tab interfaces must function as standard links when JavaScript is unavailable.

User Experience Behaviour Supported
Users can access all content without scripting.

414. Tabs Role Application Test

Source:

Requirement
Enhanced tab interfaces must use role="tablist", role="tab", and role="tabpanel".

User Experience Behaviour Supported
Users receive correct component semantics.

415. Tabs Selection State Test

Source:

Requirement
Tabs must indicate the selected state using aria-selected.

User Experience Behaviour Supported
Users understand which panel is active.

416. Tabs Panel Labelling Test

Source:

Requirement
Each tab panel must be labelled via aria-labelledby referencing its corresponding tab.

User Experience Behaviour Supported
Users can identify the relationship between tabs and panels.

417. Tabs Content Visibility Test

Source:

Requirement
Non-active tab panels must be hidden from both visual display and assistive technologies.

User Experience Behaviour Supported
Users are not exposed to irrelevant content.

418. Mega Menu Control Semantics Test

Source:

Requirement
Mega menu triggers must be implemented as button elements.

User Experience Behaviour Supported
Users can operate menus using standard interaction patterns.

419. Mega Menu aria-controls Association Test

Source:

Requirement
Menu controls must reference their associated panels via aria-controls.

User Experience Behaviour Supported
Users understand relationships between controls and content.

420. Mega Menu State Management Test

Source:

Requirement
aria-expanded must reflect whether a menu panel is open or closed.

User Experience Behaviour Supported
Users can determine menu state.

421. Mega Menu Single Panel Visibility Test

Source:

Requirement
Only one mega menu panel may be visible at a time.

User Experience Behaviour Supported
Users avoid confusion from multiple overlapping panels.

422. Mega Menu Dismissal Behaviour Test

Source:

Requirement
Panels must close when focus leaves, Escape is pressed, or the user clicks outside.

User Experience Behaviour Supported
Users retain control and avoid persistent overlays.

423. Modal Dialog Role Assignment Test

Source:

Requirement
Modal dialogs must use appropriate roles (dialog or alertdialog) depending on urgency.

User Experience Behaviour Supported
Users understand the importance and context of the dialog.

424. Modal aria-modal Declaration Test

Source:

Requirement
Modal dialogs must include aria-modal="true".

User Experience Behaviour Supported
Users are informed that interaction is restricted to the dialog.

425. Modal Initial Hidden State Test

Source:

Requirement
Dialogs must be hidden from both visual display and assistive technologies until activated.

User Experience Behaviour Supported
Users are not exposed to inactive modal content.

426. Modal Accessible Labelling Test

Source:

Requirement
Dialogs must be labelled using aria-labelledby referencing a visible heading.

User Experience Behaviour Supported
Users can identify the dialog purpose.

427. Modal Focus Placement Test

Source:

Requirement
Focus must move to a meaningful element within the dialog when opened.

User Experience Behaviour Supported
Users can immediately engage with dialog content.

428. Rating Display Text Alternative Test

Source:

Requirement
Graphical rating stars must be accompanied by a clear textual representation of the rating.

User Experience Behaviour Supported
Users understand rating values without interpreting icons.

429. Rating Icon Accessibility Test

Source:

Requirement
Decorative star icons must be hidden from assistive technologies using aria-hidden.

User Experience Behaviour Supported
Users are not exposed to redundant or confusing icon descriptions.

430. Rating Input Semantic Structure Test

Source:

Requirement
Interactive rating components must be built using semantic form controls (e.g. radio inputs).

User Experience Behaviour Supported
Users can interact with rating inputs reliably across devices.

431. Rating Touch Target Size Test

Source:

Requirement
Interactive rating controls must provide sufficiently large touch targets.

User Experience Behaviour Supported
Users can accurately select ratings, particularly on touch devices.

432. Rating High Contrast Compatibility Test

Source:

Requirement
Rating visuals must not rely solely on background images that disappear in high contrast modes.

User Experience Behaviour Supported
Users can perceive rating information in all display modes.




