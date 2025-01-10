<?php
/**
 * Widgets class.
 *
 * @category   Class
 * @package    ElementorCustom
 * @subpackage WordPress
 * @author     Maxime Pierron <maxime@pierron.com>
 * @copyright  2023 Maxime Pierron
 * @license    https://opensource.org/licenses/GPL-3.0 GPL-3.0-only
 * @link       link(https://example.com/,
 *             Build Custom Elementor Widgets)
 * @since      1.0.0
 * php version 8.2.3
 */

namespace ElementorCustom;

// Security Note: Blocks direct access to the plugin PHP files.
defined( 'ABSPATH' ) || die();

/**
 * Class Plugin
 *
 * Main Plugin class
 *
 * @since 1.0.0
 */
class Widgets {

	/**
	 * Instance
	 *
	 * @since 1.0.0
	 * @access private
	 * @static
	 *
	 * @var Plugin The single instance of the class.
	 */
	private static $instance = null;

	/**
	 * Instance
	 *
	 * Ensures only one instance of the class is loaded or can be loaded.
	 *
	 * @since 1.0.0
	 * @access public
	 *
	 * @return Plugin An instance of the class.
	 */
	public static function instance() {
		if ( is_null( self::$instance ) ) {
			self::$instance = new self();
		}

		return self::$instance;
	}

	/**
	 * Include Widgets files
	 *
	 * Load widgets files
	 *
	 * @since 1.0.0
	 * @access private
	 */
	private function include_widgets_files() {
		require_once 'widgets/class-living-shapes.php';
		require_once 'widgets/class-mouse-move-image-gallery.php';
		require_once 'widgets/class-parallax-menu.php';
		require_once 'widgets/class-futuristic-card.php';
		require_once 'widgets/class-special-hover-card.php';
		require_once 'widgets/class-special-text-block.php';
		require_once 'widgets/class-parallax-gallery.php';
	}

	/**
	 * Register Widgets
	 *
	 * Register new Elementor widgets.
	 *
	 * @since 1.0.0
	 * @access public
	 */
	public function register_widgets() {
		// It's now safe to include Widgets files.
		$this->include_widgets_files();

		// Register the plugin widget classes.
		\Elementor\Plugin::instance()->widgets_manager->register_widget_type( new Widgets\LivingShapes() );
		\Elementor\Plugin::instance()->widgets_manager->register_widget_type( new Widgets\MouseMoveImageGallery() );
		\Elementor\Plugin::instance()->widgets_manager->register_widget_type( new Widgets\ParallaxMenu() );
		\Elementor\Plugin::instance()->widgets_manager->register_widget_type( new Widgets\FuturisticCard() );
		\Elementor\Plugin::instance()->widgets_manager->register_widget_type( new Widgets\SpecialHoverCard() );
		\Elementor\Plugin::instance()->widgets_manager->register_widget_type( new Widgets\SpecialTextBlock() );
		\Elementor\Plugin::instance()->widgets_manager->register_widget_type( new Widgets\ParallaxGallery() );
	}


	/**
	 *  Plugin class constructor
	 *
	 * Register plugin action hooks and filters
	 *
	 * @since 1.0.0
	 * @access public
	 */
	public function __construct() {
		// Register the widgets.
		add_action( 'elementor/widgets/widgets_registered', array( $this, 'register_widgets' ) );
		add_action( 'elementor/elements/categories_registered', array( $this, 'add_elementor_widget_categories' ) );
	}

	function add_elementor_widget_categories( $elements_manager ) {

		$elements_manager->add_category(
			'elementor-custom-widgets',
			[
				'title' => esc_html__( 'Elementor Custom Widgets', 'elementor-custom' ),
				'icon' => 'eicon-star',
			]
		);

	}
}

// Instantiate the Widgets class.
Widgets::instance();
