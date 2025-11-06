#ifndef slic3r_AppColors_hpp_
#define slic3r_AppColors_hpp_

// ============================================================================
// Adartys Brand Color Definitions
// ============================================================================
//
// This file contains all centralized color definitions for the Adartys Slicer.
// All colors are defined here to ensure consistency and easy maintenance.
//
// IMPORTANT: When changing the primary brand color, update all related colors:
//   - Primary color (main brand color)
//   - Primary color dark mode variant
//   - Opacity variants (25%, 10%) for both light and dark modes
//
// ============================================================================

// Primary Brand Color
// Main brand color used throughout the application for highlights, selections,
// and active states
#define ADARTYS_PRIMARY_COLOR           "#892410"  // RGB(137, 36, 16) - Rust Red
#define ADARTYS_PRIMARY_COLOR_DARK      "#5C1808"  // RGB(92, 24, 8) - Dark Mode variant
#define ADARTYS_PRIMARY_HEX             0x892410   // Hex value for wxColour(0xRRGGBB) constructor
#define ADARTYS_PRIMARY_RGB             137, 36, 16 // RGB values for wxColour(r,g,b) constructor

// Secondary/Variant Colors (calculated from primary)
// These are lighter/darker variants of the primary color
#define ADARTYS_PRIMARY_HOVER           "#B84E2F"  // RGB(184, 78, 47) - Hover state (~35% lighter)
#define ADARTYS_PRIMARY_HOVER_RGB       184, 78, 47 // RGB values for hover state
#define ADARTYS_PRIMARY_HOVER_HEX       0xB84E2F   // Hex value for hover state

// Primary Color with 25% Opacity
// Used for dropdown checked items, selected backgrounds, and hover states
#define ADARTYS_PRIMARY_25_OPACITY      "#D9A597"  // RGB(217, 165, 151) - 25% on white
#define ADARTYS_PRIMARY_25_OPACITY_DARK "#2B1612"  // RGB(43, 22, 18) - 25% on dark
#define ADARTYS_PRIMARY_25_OPACITY_HEX  0xD9A597   // Hex value for wxColour(0xRRGGBB)

// Primary Color with 10% Opacity
// Used for combo boxes, dropdown focused backgrounds, and subtle highlights
#define ADARTYS_PRIMARY_10_OPACITY      "#F2E7E6"  // RGB(242, 231, 230) - 10% on white
#define ADARTYS_PRIMARY_10_OPACITY_DARK "#1E0F0C"  // RGB(30, 15, 12) - 10% on dark
#define ADARTYS_PRIMARY_10_OPACITY_HEX  0xF2E7E6   // Hex value for wxColour(0xRRGGBB)

// Secondary Brand Color
// Used as accent color for warnings, notifications, and secondary actions
#define ADARTYS_SECONDARY_COLOR         "#FF6F00"  // RGB(255, 111, 0) - Orange (unchanged)

// ============================================================================
// Color Calculation Notes
// ============================================================================
//
// Opacity calculations (color blending with background):
//   For light mode (white background #FFFFFF):
//     Final = (Color * opacity) + (255 * (1 - opacity))
//
//   For dark mode (dark background):
//     Final = (Color * opacity) + (Background * (1 - opacity))
//
// Example for 25% opacity on white:
//   R = 137 * 0.25 + 255 * 0.75 = 225.25 ≈ 217
//   G = 36 * 0.25 + 255 * 0.75 = 200.25 ≈ 165
//   B = 16 * 0.25 + 255 * 0.75 = 195.25 ≈ 151
//   Result: #D9A597
//
// ============================================================================

#endif // slic3r_AppColors_hpp_
