<?php
/**
 * ParallaxGallery class.
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
namespace ElementorCustom\Widgets;

use ElementorPro\Base\Base_Widget;
use Elementor\Controls_Manager;
// Security Note: Blocks direct access to the plugin PHP files.
defined( 'ABSPATH' ) || die();
/**
 * ParallaxGallery widget class.
 *
 * @since 1.0.0
 */
class ParallaxGallery extends Base_Widget {
	/**
	 * Class constructor.
	 *
	 * @param array $data Widget data.
	 * @param array $args Widget arguments.
	 */
	public function __construct( $data = array(), $args = null ) {
		parent::__construct( $data, $args );
		wp_register_style( 'parallaxgallery', plugins_url( '/assets/css/parallaxgallery.css', ELEMENTOR_CUSTOM ), array(), '1.0.0' );
		wp_register_script( 'parallaxgallery', plugins_url( '/assets/js/parallaxgallery.js', ELEMENTOR_CUSTOM ), array(), '1.0.0' );
	}
	/**
	 * Retrieve the widget name.
	 *
	 * @since 1.0.0
	 *
	 * @access public
	 *
	 * @return string Widget name.
	 */
	public function get_name() {
		return 'parallax-gallery';
	}
	/**
	 * Retrieve the widget title.
	 *
	 * @since 1.0.0
	 *
	 * @access public
	 *
	 * @return string Widget title.
	 */
	public function get_title() {
		return __( 'Parallax Gallery', 'elementor-custom' );
	}
	/**
	 * Retrieve the widget icon.
	 *
	 * @since 1.0.0
	 *
	 * @access public
	 *
	 * @return string Widget icon.
	 */
	public function get_icon() {
		return 'eicon-parallax';
	}
	/**
	 * Retrieve the list of categories the widget belongs to.
	 *
	 * Used to determine where to display the widget in the editor.
	 *
	 * Note that currently Elementor supports only one category.
	 * When multiple categories passed, Elementor uses the first one.
	 *
	 * @since 1.0.0
	 *
	 * @access public
	 *
	 * @return array Widget categories.
	 */
	public function get_categories() {
		return array( 'elementor-custom-widgets' );
	}
	
	/**
	 * Enqueue styles.
	 */
	public function get_style_depends() {
		return array( 'parallaxgallery' );
	}
	/**
	 * Enqueue scripts.
	 */
	public function get_script_depends() {
		if (\Elementor\Plugin::$instance->editor->is_edit_mode() || \Elementor\Plugin::$instance->preview->is_preview_mode()) {
			return [];
		} else {
			return array( 'parallaxgallery' );
		}
		
	}

	/**
	 * Register the widget controls.
	 *
	 * Adds different input fields to allow the user to change and customize the widget settings.
	 *
	 * @since 1.0.0
	 *
	 * @access protected
	 */
	protected function _register_controls() {

		$this->start_controls_section(
			'content_section',
			[
				'label' => __( 'Content', 'elementor-custom' ),
				'tab' => \Elementor\Controls_Manager::TAB_CONTENT,
			]
		);

        $this->add_control(
			'background_color',
			[
				'label' => esc_html__( 'Background Color', 'elementor-custom' ),
				'type' => \Elementor\Controls_Manager::COLOR,
				'selectors' => [
					'{{WRAPPER}} .parallax-gallery' => 'background-color: {{VALUE}}',
				],
                'default' => 'rgb(20, 20, 20)'
			]
		);

		$this->add_control(
			'parallax_gallery',
			[
				'label' => esc_html__( 'Add Images', 'textdomain' ),
				'type' => \Elementor\Controls_Manager::GALLERY,
				'show_label' => false,
				'default' => [
                    [
                        'id' => 0,
                        'url' => 'https://images.unsplash.com/photo-1524781289445-ddf8f5695861?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1770&q=80'
                    ],
                    [
                        'id' => 1,
                        'url' => 'https://images.unsplash.com/photo-1610194352361-4c81a6a8967e?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1674&q=80'
                    ],
                    [
                        'id' => 2,
                        'url' => 'https://images.unsplash.com/photo-1618202133208-2907bebba9e1?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1770&q=80'
                    ],
                    [
                        'id' => 3,
                        'url' => 'https://images.unsplash.com/photo-1495805442109-bf1cf975750b?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1770&q=80'
                    ],
                    [
                        'id' => 4,
                        'url' => 'https://images.unsplash.com/photo-1548021682-1720ed403a5b?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1770&q=80'
                    ],
                    [
                        'id' => 5,
                        'url' => 'https://images.unsplash.com/photo-1496753480864-3e588e0269b3?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2134&q=80'
                    ],
                    [
                        'id' => 6,
                        'url' => 'https://images.unsplash.com/photo-1613346945084-35cccc812dd5?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1759&q=80'
                    ],
                    [
                        'id' => 7,
                        'url' => 'https://images.unsplash.com/photo-1516681100942-77d8e7f9dd97?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1770&q=80'
                    ],
                ],
			]
		);

		$this->end_controls_section();
	}
	/**
	 * Render the widget output on the frontend.
	 *
	 * Written in PHP and used to generate the final HTML.
	 *
	 * @since 1.0.0
	 *
	 * @access protected
	 */
	protected function render() {
		$settings = $this->get_settings_for_display();
        ?>
        <div class="parallax-gallery">
            <div id="image-track" data-mouse-down-at="0" data-prev-percentage="0">
        <?php
                if ( $settings['parallax_gallery'] ) {
                    foreach (  $settings['parallax_gallery'] as $key=>$image ) {
                        echo '<img class="parallax-gallery-image parallax-gallery-image-'. $key .'" src="' . esc_attr($image['url']) . '" draggable="false">';
                    }
                }
        ?>
            </div>
        </div>
        <?php
	}

	protected function content_template() {
		?>
        <div class="parallax-gallery">
            <div id="image-track" data-mouse-down-at="0" data-prev-percentage="0">
                <# if ( settings.parallax_gallery ) { #>
                    <# _.each( settings.parallax_gallery, function( image, index) { #>
                    <img class="parallax-gallery-image parallax-gallery-image-{{index}}" src="{{image.url}}">
                <# }); #>
                <# } #>
            </div>
        </div>
		<?php
	}
}