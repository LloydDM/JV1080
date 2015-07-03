'''
Created on Feb 20, 2015

@author: David

MIDI Address map for the JV-1080
'''

PATCH_MODE = {'Patch Common': 0,
              'Patch Tone 1': 16,
              'Patch Tone 2': 18,
              'Patch Tone 2': 20,
              'Patch Tone 4': 22
              }

PATCH_COMMON = ('Patch Name 1',
                'Patch Name 2',
                'Patch Name 3',
                'Patch Name 4',
                'Patch Name 5',
                'Patch Name 6',
                'Patch Name 7',
                'Patch Name 8',
                'Patch Name 9',
                'Patch Name 10',
                'Patch Name 11',
                'Patch Name 12',
                'EFX:Type',
                'EFX:Parameter 1',
                'EFX:Parameter 2',
                'EFX:Parameter 3',
                'EFX:Parameter 4',
                'EFX:Parameter 5',
                'EFX:Parameter 6',
                'EFX:Parameter 7',
                'EFX:Parameter 8',
                'EFX:Parameter 9',
                'EFX:Parameter 10',
                'EFX:Parameter 11',
                'EFX:Parameter 12',
                'EFX:Output Assign',
                'EFX:Output Level',
                'EFX:Chorus Send Level',
                'EFX:Reverb Send Level',
                'EFX:Control Source 1',
                'EFX:Control Depth 1',
                'EFX:Control Source 2',
                'EFX:Control Depth 2',
                'Chorus:Level',
                'Chorus:Rate',
                'Chorus:Depth',
                'Chorus:Pre Delay',
                'Chorus:Feedback',
                'Chorus:Output Assign',
                'Reverb:Type',
                'Reverb:Level',
                'Reverb:Time',
                'Reverb:HF Damp',
                'Reverb:Feedback',
                'Default Tempo', # Requires split-byte send
                'Patch Level',
                'Patch Pan',
                'Analog Feel Depth',
                'Bender Range Up',
                'Bender Range Down',
                'Key Assign Mode',
                'Solo Legato',
                'Portamento Switch',
                'Portamento Mode',
                'Portamento Type',
                'Portamento Start',
                'Portamento Time',
                'Patch Control Source 2',
                'Patch Control Source 3',
                'EFX Control Hold/Peak',
                'Control 1 Hold/Peak',
                'Control 2 Hold/Peak',
                'Control 3 Hold/Peak',
                'Velocity Range Switch',
                'Octave Shift',
                'Stretch Tune Depth',
                'Voice Priority',
                'Structure Type 1 & 2',
                'Booster Level 1 & 2',
                'Structure Type 3 & 4',
                'Booster Level 3 & 4'
                )

PATCH_TONE = ('Tone Switch',
              'Wave Group',
              'Wave Group ID',
              'Wave Number', # Requires split-byte send
              'Wave Gain',
              'FXM Switch',
              'FXM Color',
              'FXM Depth',
              'Tone Delay Mode',
              'Tone Delay Time',
              'Velocity Cross Fade Depth',
              'Velocity Range Lower',
              'Velocity Range Upper',
              'Key Range Lower',
              'Key Range Upper',
              'Redamper Control Switch',
              'Volume Control Switch',
              'Hold-1 Control Switch',
              'Bender Control Switch',
              'Pan Control Switch',
              'Controller 1 Destination 1',
              'Controller 1 Depth 1',
              'Controller 1 Destination 2',
              'Controller 1 Depth 2',
              'Controller 1 Destination 3',
              'Controller 1 Depth 3',
              'Controller 1 Destination 4',
              'Controller 1 Depth 4',
              'Controller 2 Destination 1',
              'Controller 2 Depth 1',
              'Controller 2 Destination 2',
              'Controller 2 Depth 2',
              'Controller 2 Destination 3',
              'Controller 2 Depth 3',
              'Controller 2 Destination 4',
              'Controller 2 Depth 4',
              'Controller 3 Destination 1',
              'Controller 3 Depth 1',
              'Controller 3 Destination 2',
              'Controller 3 Depth 2',
              'Controller 3 Destination 3',
              'Controller 3 Depth 3',
              'Controller 3 Destination 4',
              'Controller 3 Depth 4',
              'LFO 1 Waveform',
              'LFO 1 Key Trigger',
              'LFO 1 Rate',
              'LFO 1 Level Offset',
              'LFO 1 Delay Time',
              'LFO 1 Fade Mode',
              'LFO 1 Fade Time',
              'LFO 1 External Sync',
              'LFO 2 Waveform',
              'LFO 2 Key Trigger',
              'LFO 2 Rate',
              'LFO 2 Level Offset',
              'LFO 2 Delay Time',
              'LFO 2 Fade Mode',
              'LFO 2 Fade Time',
              'LFO 2 External Sync',
              'Coarse Tune',
              'Fine Tune',
              'Random Pitch Depth',
              'Pitch Keyfollow',
              'P-ENV Depth',
              'P-ENV Velocity Sensitivity',
              'P-ENV Velocity Time 1 Sensitivity',
              'P-ENV Velocity Time 4 Sensitivity',
              'P-ENV Time Keyfollow',
              'P-ENV Time 1',
              'P-ENV Time 2',
              'P-ENV Time 3',
              'P-ENV Time 4',
              'P-ENV Level 1',
              'P-ENV Level 2',
              'P-ENV Level 3',
              'P-ENV Level 4',
              'Pitch LFO Depth 1',
              'Pitch LFO Depth 2',
              'Filter Type',
              'Cutoff Frequency',
              'Cutoff Keyfollow',
              'Resonance',
              'Resonance Velocity Sensitivity',
              'F-ENV Depth',
              'F-ENV Velocity Curve',
              'F-ENV Velocity Sensitivity',
              'F-ENV Velocity Time 1 Sensitivity',
              'F-ENV Velocity Time 4 Sensitivity',
              'F-ENV Time Keyfollow',
              'F-ENV Time 1',
              'F-ENV Time 2',
              'F-ENV Time 3',
              'F-ENV Time 4',
              'F-ENV Level 1',
              'F-ENV Level 2',
              'F-ENV Level 3',
              'F-ENV Level 4',
              'Filter LFO 1 Depth',
              'Filter LFO 2 Depth',
              'Tone Level',
              'Bias Direction',
              'Bias Point',
              'Bias Level',
              'A-ENV Velocity Curve',
              'A-ENV Velocity Sensitivity',
              'A-ENV Velocity Time 1 Sensitivity',
              'A-ENV Velocity Time 4 Sensitivity',
              'A-ENV Time Keyfollow',
              'A-ENV Time 1',
              'A-ENV Time 2',
              'A-ENV Time 3',
              'A-ENV Time 4',
              'A-ENV Level 1',
              'A-ENV Level 2',
              'A-ENV Level 3',
              'Amplitude LFO 1 Depth',
              'Amplitude LFO 2 Depth',
              'Tone Pan',
              'Pan Keyfollow',
              'Random Pan Depth',
              'Alternate Pan Depth',
              'Pan LFO 1 Depth',
              'Pan LFO 2 Depth',
              'Output Assign',
              'Output Level',
              'Chorus Send Level',
              'Reverb Send Level'
              )