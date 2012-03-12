import bpy
import os

wm = bpy.context.window_manager
kc = wm.keyconfigs.new(os.path.splitext(os.path.basename(__file__))[0])

# Map Screen
km = kc.keymaps.new('Screen', space_type='EMPTY', region_type='WINDOW', modal=False)

kmi = km.keymap_items.new('screen.animation_step', 'TIMER0', 'ANY', any=True)
kmi = km.keymap_items.new('screen.screen_set', 'RIGHT_ARROW', 'PRESS', ctrl=True)
kmi.properties.delta = 1
kmi = km.keymap_items.new('screen.screen_set', 'LEFT_ARROW', 'PRESS', ctrl=True)
kmi.properties.delta = -1
kmi = km.keymap_items.new('screen.screen_full_area', 'UP_ARROW', 'PRESS', ctrl=True)
kmi = km.keymap_items.new('screen.screen_full_area', 'DOWN_ARROW', 'PRESS', ctrl=True)
kmi = km.keymap_items.new('screen.screen_full_area', 'SPACE', 'PRESS', shift=True)
kmi = km.keymap_items.new('screen.screenshot', 'F3', 'PRESS', ctrl=True)
kmi = km.keymap_items.new('screen.screencast', 'F3', 'PRESS', alt=True)
kmi = km.keymap_items.new('screen.region_quadview', 'Q', 'PRESS', ctrl=True, alt=True)
kmi = km.keymap_items.new('screen.repeat_history', 'F3', 'PRESS')
kmi = km.keymap_items.new('screen.repeat_last', 'R', 'PRESS', shift=True)
kmi = km.keymap_items.new('screen.region_flip', 'F5', 'PRESS')
kmi = km.keymap_items.new('screen.redo_last', 'F6', 'PRESS')
kmi = km.keymap_items.new('script.reload', 'F8', 'PRESS')
kmi = km.keymap_items.new('file.execute', 'RET', 'PRESS')
kmi = km.keymap_items.new('file.execute', 'NUMPAD_ENTER', 'PRESS')
kmi = km.keymap_items.new('file.cancel', 'ESC', 'PRESS')
kmi = km.keymap_items.new('ed.undo', 'Z', 'PRESS', oskey=True)
kmi = km.keymap_items.new('ed.redo', 'Z', 'PRESS', shift=True, oskey=True)
kmi = km.keymap_items.new('ed.undo_history', 'Z', 'PRESS', alt=True, oskey=True)
kmi = km.keymap_items.new('ed.undo', 'Z', 'PRESS', ctrl=True)
kmi = km.keymap_items.new('ed.redo', 'Z', 'PRESS', shift=True, ctrl=True)
kmi = km.keymap_items.new('ed.undo_history', 'Z', 'PRESS', ctrl=True, alt=True)
kmi = km.keymap_items.new('render.render', 'SLASH', 'PRESS', shift=True)
kmi = km.keymap_items.new('render.render', 'F12', 'PRESS', ctrl=True)
kmi.properties.animation = True
kmi = km.keymap_items.new('render.view_cancel', 'ESC', 'PRESS')
kmi = km.keymap_items.new('render.view_show', 'F11', 'PRESS')
kmi = km.keymap_items.new('render.play_rendered_anim', 'F11', 'PRESS', ctrl=True)
kmi = km.keymap_items.new('screen.userpref_show', 'COMMA', 'PRESS', oskey=True)
kmi = km.keymap_items.new('screen.userpref_show', 'U', 'PRESS', ctrl=True, alt=True)

# Map Mesh
km = kc.keymaps.new('Mesh', space_type='EMPTY', region_type='WINDOW', modal=False)

kmi = km.keymap_items.new('mesh.loopcut_slide', 'R', 'PRESS', ctrl=True)
kmi = km.keymap_items.new('mesh.loop_select', 'SELECTMOUSE', 'PRESS', ctrl=True)
kmi = km.keymap_items.new('mesh.loop_select', 'SELECTMOUSE', 'PRESS', shift=True, alt=True)
kmi.properties.extend = True
kmi = km.keymap_items.new('mesh.edgering_select', 'SELECTMOUSE', 'PRESS', ctrl=True, alt=True)
kmi = km.keymap_items.new('mesh.edgering_select', 'SELECTMOUSE', 'PRESS', shift=True, ctrl=True, alt=True)
kmi.properties.extend = True
kmi = km.keymap_items.new('mesh.select_shortest_path', 'SELECTMOUSE', 'PRESS', ctrl=True)
kmi = km.keymap_items.new('mesh.select_all', 'A', 'PRESS')
kmi = km.keymap_items.new('mesh.select_more', 'NUMPAD_PLUS', 'PRESS', ctrl=True)
kmi = km.keymap_items.new('mesh.select_less', 'NUMPAD_MINUS', 'PRESS', ctrl=True)
kmi = km.keymap_items.new('mesh.select_inverse', 'I', 'PRESS', ctrl=True)
kmi = km.keymap_items.new('mesh.select_non_manifold', 'M', 'PRESS', shift=True, ctrl=True, alt=True)
kmi = km.keymap_items.new('mesh.select_linked', 'L', 'PRESS', ctrl=True)
kmi = km.keymap_items.new('mesh.select_linked_pick', 'L', 'PRESS')
kmi = km.keymap_items.new('mesh.select_linked_pick', 'L', 'PRESS', shift=True)
kmi.properties.deselect = True
kmi = km.keymap_items.new('mesh.faces_select_linked_flat', 'F', 'PRESS', shift=True, ctrl=True, alt=True)
kmi = km.keymap_items.new('mesh.select_similar', 'G', 'PRESS', shift=True)
kmi = km.keymap_items.new('wm.call_menu', 'TAB', 'PRESS', ctrl=True)
kmi.properties.name = 'VIEW3D_MT_edit_mesh_select_mode'
kmi = km.keymap_items.new('mesh.hide', 'H', 'PRESS')
kmi = km.keymap_items.new('mesh.hide', 'H', 'PRESS', shift=True)
kmi.properties.unselected = True
kmi = km.keymap_items.new('mesh.reveal', 'H', 'PRESS', alt=True)
kmi = km.keymap_items.new('mesh.normals_make_consistent', 'N', 'PRESS', ctrl=True)
kmi = km.keymap_items.new('mesh.normals_make_consistent', 'N', 'PRESS', shift=True, ctrl=True)
kmi.properties.inside = True
kmi = km.keymap_items.new('view3d.edit_mesh_extrude_move_normal', 'E', 'PRESS')
kmi = km.keymap_items.new('wm.call_menu', 'E', 'PRESS', alt=True)
kmi.properties.name = 'VIEW3D_MT_edit_mesh_extrude'
kmi = km.keymap_items.new('transform.edge_crease', 'E', 'PRESS', shift=True)
kmi = km.keymap_items.new('mesh.spin', 'R', 'PRESS', alt=True)
kmi = km.keymap_items.new('mesh.fill', 'F', 'PRESS', alt=True)
kmi = km.keymap_items.new('mesh.beautify_fill', 'F', 'PRESS', shift=True, alt=True)
kmi = km.keymap_items.new('mesh.quads_convert_to_tris', 'T', 'PRESS', ctrl=True)
kmi = km.keymap_items.new('mesh.tris_convert_to_quads', 'J', 'PRESS', alt=True)
kmi = km.keymap_items.new('mesh.edge_flip', 'F', 'PRESS', shift=True, ctrl=True)
kmi = km.keymap_items.new('mesh.rip_move', 'V', 'PRESS')
kmi = km.keymap_items.new('mesh.merge', 'M', 'PRESS', alt=True)
kmi = km.keymap_items.new('transform.shrink_fatten', 'S', 'PRESS', alt=True)
kmi = km.keymap_items.new('mesh.edge_face_add', 'F', 'PRESS')
kmi = km.keymap_items.new('mesh.duplicate_move', 'D', 'PRESS', shift=True)
kmi = km.keymap_items.new('wm.call_menu', 'A', 'PRESS', shift=True)
kmi.properties.name = 'INFO_MT_mesh_add'
kmi = km.keymap_items.new('mesh.separate', 'P', 'PRESS')
kmi = km.keymap_items.new('mesh.split', 'Y', 'PRESS')
kmi = km.keymap_items.new('mesh.dupli_extrude_cursor', 'ACTIONMOUSE', 'CLICK', ctrl=True)
kmi = km.keymap_items.new('mesh.dupli_extrude_cursor', 'ACTIONMOUSE', 'CLICK', shift=True, ctrl=True)
kmi.properties.rotate_source = False
kmi = km.keymap_items.new('mesh.delete', 'X', 'PRESS')
kmi = km.keymap_items.new('mesh.delete', 'DEL', 'PRESS')
kmi = km.keymap_items.new('mesh.knife_cut', 'LEFTMOUSE', 'PRESS', key_modifier='K')
kmi = km.keymap_items.new('mesh.knife_cut', 'LEFTMOUSE', 'PRESS', shift=True, key_modifier='K')
kmi.properties.type = 'MIDPOINTS'
kmi = km.keymap_items.new('object.vertex_parent_set', 'P', 'PRESS', ctrl=True)
kmi = km.keymap_items.new('wm.call_menu', 'W', 'PRESS')
kmi.properties.name = 'VIEW3D_MT_edit_mesh_specials'
kmi = km.keymap_items.new('wm.call_menu', 'F', 'PRESS', ctrl=True)
kmi.properties.name = 'VIEW3D_MT_edit_mesh_faces'
kmi = km.keymap_items.new('wm.call_menu', 'E', 'PRESS', ctrl=True)
kmi.properties.name = 'VIEW3D_MT_edit_mesh_edges'
kmi = km.keymap_items.new('wm.call_menu', 'V', 'PRESS', ctrl=True)
kmi.properties.name = 'VIEW3D_MT_edit_mesh_vertices'
kmi = km.keymap_items.new('wm.call_menu', 'H', 'PRESS', ctrl=True)
kmi.properties.name = 'VIEW3D_MT_hook'
kmi = km.keymap_items.new('wm.call_menu', 'U', 'PRESS')
kmi.properties.name = 'VIEW3D_MT_uv_map'
kmi = km.keymap_items.new('wm.call_menu', 'G', 'PRESS', ctrl=True)
kmi.properties.name = 'VIEW3D_MT_vertex_group'
kmi = km.keymap_items.new('object.subdivision_set', 'ZERO', 'PRESS', ctrl=True)
kmi.properties.level = 0
kmi = km.keymap_items.new('object.subdivision_set', 'ONE', 'PRESS', ctrl=True)
kmi.properties.level = 1
kmi = km.keymap_items.new('object.subdivision_set', 'TWO', 'PRESS', ctrl=True)
kmi.properties.level = 2
kmi = km.keymap_items.new('object.subdivision_set', 'THREE', 'PRESS', ctrl=True)
kmi.properties.level = 3
kmi = km.keymap_items.new('object.subdivision_set', 'FOUR', 'PRESS', ctrl=True)
kmi.properties.level = 4
kmi = km.keymap_items.new('object.subdivision_set', 'FIVE', 'PRESS', ctrl=True)
kmi.properties.level = 5
kmi = km.keymap_items.new('wm.context_cycle_enum', 'O', 'PRESS', shift=True)
kmi.properties.data_path = 'tool_settings.proportional_edit_falloff'
kmi = km.keymap_items.new('wm.context_toggle_enum', 'O', 'PRESS')
kmi.properties.data_path = 'tool_settings.proportional_edit'
kmi.properties.value_1 = 'DISABLED'
kmi.properties.value_2 = 'ENABLED'
kmi = km.keymap_items.new('wm.context_toggle_enum', 'O', 'PRESS', alt=True)
kmi.properties.data_path = 'tool_settings.proportional_edit'
kmi.properties.value_1 = 'DISABLED'
kmi.properties.value_2 = 'CONNECTED'

