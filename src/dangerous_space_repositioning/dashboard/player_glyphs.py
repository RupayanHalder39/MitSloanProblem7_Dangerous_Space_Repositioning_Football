"""Project-local procedural footballer glyph helpers.

Migrated from the project-controlled ``offside_break`` dashboard so this
project does not import a sibling research package. No assets are loaded.
"""
import math
import cv2
import numpy as np

GLYPH_SCALE_MIN, GLYPH_SCALE_MAX = 0.60, 1.45
HUMAN_GLYPH_BASE_H = 22.0
HUMAN_HEAD_FRAC, HUMAN_NECK_FRAC = 0.15, 0.05
HUMAN_TORSO_FRAC, HUMAN_HIP_FRAC, HUMAN_LEG_FRAC = 0.35, 0.125, 0.375
HEADING_MIN_SPEED_CM_S, HEADING_LOOKAHEAD_SEC = 80.0, 0.3

def _player_glyph_colors(team_color):
    return tuple(int(max(0, c * 0.55)) for c in team_color), tuple(int(min(255, c * 1.18 + 20)) for c in team_color)

def _heading_cue(dx, dy):
    norm = math.hypot(dx, dy)
    return (1.0, 0.0, 0.0) if norm < 1e-6 else (1.0 if dx >= 0 else -1.0, dx / norm, dy / norm)

def _draw_player_shadow(img, px, py, scale=1.0):
    s = max(GLYPH_SCALE_MIN, min(GLYPH_SCALE_MAX, float(scale)))
    cv2.ellipse(img, (px, py + 1), (max(3, round(5.5 * s)), max(1, round(2 * s))), 0, 0, 360, (8, 8, 8), -1, cv2.LINE_AA)

def _draw_player_body_human(img, px, py, team_color, scale=1.0, mirror_sign=1.0, lean=(0.0, 0.0), outline=(10, 10, 10)):
    s = max(GLYPH_SCALE_MIN, min(GLYPH_SCALE_MAX, float(scale))); h = HUMAN_GLYPH_BASE_H * s
    head_r=max(2,round(h*HUMAN_HEAD_FRAC/2)); neck_h=max(1,round(h*HUMAN_NECK_FRAC)); torso_h=max(3,round(h*HUMAN_TORSO_FRAC)); hip_h=max(2,round(h*HUMAN_HIP_FRAC)); leg_h=max(3,round(h*HUMAN_LEG_FRAC))
    shoulder_half=max(2,round(h*.18)); waist_half=max(2,round(h*.11)); shorts_half=max(2,round(h*.13)); leg_half=max(2,round(h*.09)); arm_len=max(2,round(h*.20))
    leg_stagger=max(1,round(leg_h*.18))*mirror_sign; arm_stagger=max(1,round(arm_len*.5))*mirror_sign; lean_px=min(1.6,1.6*s)
    def pt(r,f,upper=False): return int(round(px+r+(lean[0]*lean_px if upper else 0))), int(round(py-f+(lean[1]*lean_px if upper else 0)))
    hip=leg_h; waist=leg_h+hip_h; shoulder=waist+torso_h; neck_top=shoulder+neck_h; head=neck_top+head_r
    dark,_=_player_glyph_colors(team_color); shorts_color=tuple(int(max(0,c*.7)) for c in team_color); leg_th=max(1,round(1.5*s)); foot_r=max(1,leg_th//2+1)
    cv2.line(img,pt(-leg_half,hip),pt(-leg_half,leg_stagger),dark,leg_th,cv2.LINE_AA); cv2.line(img,pt(leg_half,hip),pt(leg_half,-leg_stagger),dark,leg_th,cv2.LINE_AA)
    cv2.circle(img,pt(-leg_half,leg_stagger),foot_r,dark,-1,cv2.LINE_AA); cv2.circle(img,pt(leg_half,-leg_stagger),foot_r,dark,-1,cv2.LINE_AA)
    shorts=np.array([pt(-shorts_half,hip),pt(shorts_half,hip),pt(waist_half,waist),pt(-waist_half,waist)],dtype=np.int32); cv2.fillPoly(img,[shorts],shorts_color,cv2.LINE_AA)
    torso=np.array([pt(-waist_half,waist,True),pt(waist_half,waist,True),pt(shoulder_half,shoulder,True),pt(-shoulder_half,shoulder,True)],dtype=np.int32); cv2.fillPoly(img,[torso],team_color,cv2.LINE_AA); cv2.polylines(img,[torso],True,outline,1,cv2.LINE_AA)
    arm_th=max(1,round(1.3*s)); cv2.line(img,pt(-shoulder_half,shoulder,True),pt(-shoulder_half-arm_len,shoulder-arm_stagger,True),dark,arm_th,cv2.LINE_AA); cv2.line(img,pt(shoulder_half,shoulder,True),pt(shoulder_half+arm_len,shoulder+arm_stagger,True),dark,arm_th,cv2.LINE_AA)
    cv2.line(img,pt(0,shoulder,True),pt(0,neck_top,True),dark,max(1,round(1.4*s)),cv2.LINE_AA); cv2.circle(img,pt(0,head,True),head_r,(222,222,222),-1,cv2.LINE_AA); cv2.circle(img,pt(0,head,True),head_r,outline,1,cv2.LINE_AA)
