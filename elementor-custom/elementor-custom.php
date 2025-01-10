<?php
/**
 * Elementor Custom WordPress Plugin
 *
 * @package ElementorCustom
 *
 * Plugin Name: Elementor Custom Widgets
 * Description: Slick, clean and refreshing widgets
 * Plugin URI:  https://www.example.com
 * Version:     1.0.0
 * Author:      Maxime Pierron
 * Author URI:  https://www.maxime.pierron
 * Text Domain: elementor-customwidgets
 */
define( 'ELEMENTOR_CUSTOM', __FILE__ );
/**
 * Include the Elementor_Custom class.
 */
require plugin_dir_path( ELEMENTOR_CUSTOM ) . 'class-elementor-custom.php';