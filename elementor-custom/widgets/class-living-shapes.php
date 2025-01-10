<?php
/**
 * LivingShapes class.
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
 * LivingShapes widget class.
 *
 * @since 1.0.0
 */
class LivingShapes extends Base_Widget {
	/**
	 * Class constructor.
	 *
	 * @param array $data Widget data.
	 * @param array $args Widget arguments.
	 */
	public function __construct( $data = array(), $args = null ) {
		parent::__construct( $data, $args );
		wp_register_style( 'livingshapes', plugins_url( '/assets/css/livingshapes.css', ELEMENTOR_CUSTOM ), array(), '1.0.0' );
		wp_register_script( 'livingshapes', plugins_url( '/assets/js/livingshapes.js', ELEMENTOR_CUSTOM ), array(), '1.0.0' );
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
		return 'living-shapes';
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
		return __( 'Living Shapes', 'elementor-custom' );
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
		return 'eicon-square';
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
		return array( 'livingshapes' );
	}
	/**
	 * Enqueue scripts.
	 */
	public function get_script_depends() {
		if (\Elementor\Plugin::$instance->editor->is_edit_mode() || \Elementor\Plugin::$instance->preview->is_preview_mode()) {
			return [];
		} else {
			return array( 'livingshapes' );
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
			'Shape 1',
			[
				'label' => esc_html__( 'Shape 1 color', 'elementor-custom' ),
				'type' => \Elementor\Controls_Manager::COLOR,
				'selectors' => [
					'{{WRAPPER}} .shape-1' => 'background-color: {{VALUE}}',
				],
			]
		);
		$this->add_control(
			'Shape 2',
			[
				'label' => esc_html__( 'Shape 2 color', 'elementor-custom' ),
				'type' => \Elementor\Controls_Manager::COLOR,
				'selectors' => [
					'{{WRAPPER}} .shape-2' => 'background-color: {{VALUE}}',
				],
			]
		);
		$this->add_control(
			'Shape 3',
			[
				'label' => esc_html__( 'Shape 3 color', 'elementor-custom' ),
				'type' => \Elementor\Controls_Manager::COLOR,
				'selectors' => [
					'{{WRAPPER}} .shape-3' => 'background-color: {{VALUE}}',
				],
			]
		);
		$this->add_control(
			'Shape 4',
			[
				'label' => esc_html__( 'Shape 4 color', 'elementor-custom' ),
				'type' => \Elementor\Controls_Manager::COLOR,
				'selectors' => [
					'{{WRAPPER}} .shape-4' => 'background-color: {{VALUE}}',
				],
			]
		);
		$this->add_control(
			'Shape 5',
			[
				'label' => esc_html__( 'Shape 5 color', 'elementor-custom' ),
				'type' => \Elementor\Controls_Manager::COLOR,
				'selectors' => [
					'{{WRAPPER}} .shape-5' => 'background-color: {{VALUE}}',
				],
			]
		);
		$this->add_control(
			'Shape 6',
			[
				'label' => esc_html__( 'Shape 6 color', 'elementor-custom' ),
				'type' => \Elementor\Controls_Manager::COLOR,
				'selectors' => [
					'{{WRAPPER}} .shape-6' => 'background-color: {{VALUE}}',
				],
			]
		);
		$this->add_control(
			'Shape 7',
			[
				'label' => esc_html__( 'Shape 7 color', 'elementor-custom' ),
				'type' => \Elementor\Controls_Manager::COLOR,
				'selectors' => [
					'{{WRAPPER}} .shape-7' => 'background-color: {{VALUE}}',
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
		<div id="shapes-wrapper" data-configuration="1" data-roundness="1">
			<div class="shape shape-1"></div>
			<div class="shape shape-2"></div>
			<div class="shape shape-3"></div>
			<div class="shape shape-4"></div>
			<div class="shape shape-5"></div>
			<div class="shape shape-6"></div>
			<div class="shape shape-7"></div>
		</div>
		<?php
	}
	/**
	 * Render the widget output in the editor.
	 *
	 * Written as a Backbone JavaScript template and used to generate the live preview.
	 *
	 * @since 1.0.0
	 *
	 * @access protected
	 */
	protected function content_template() {
		?>
		<div id="shapes-wrapper" data-configuration="1" data-roundness="1">
			<div class="shape shape-1"></div>
			<div class="shape shape-2"></div>
			<div class="shape shape-3"></div>
			<div class="shape shape-4"></div>
			<div class="shape shape-5"></div>
			<div class="shape shape-6"></div>
			<div class="shape shape-7"></div>
		</div>
		<?php
	}
}